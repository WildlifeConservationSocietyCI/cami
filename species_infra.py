import os
import argparse
from argparse import RawDescriptionHelpFormatter
import arcpy
from arcpy import env
from conflict_matrix import *

env.overwriteOutput = True

parser = argparse.ArgumentParser(description=u"""
Iterate over list of species/infrastructure threat ratings and output a feature class for each combination 
representing all infrastructure features within that species' range classified by amount of barrier.
""",
                                 formatter_class=RawDescriptionHelpFormatter)
parser.add_argument('-s', '--dir_species',
                    default='C:/Users/kfisher/Documents/Asia/CAMI_species/work/data/working/post-workshop/CAMI_170616'
                            '.gdb/species',
                    help=u'Absolute path to workspace containing species feature classes.')
parser.add_argument('-i', '--dir_infra',
                    default='C:/Users/kfisher/Documents/Asia/CAMI_species/work/data/working/post-workshop/CAMI_170616'
                            '.gdb/infrastructure',
                    help=u'Absolute path to workspace containing infrastructure feature classes.')
parser.add_argument('-o', '--dir_output',
                    default='C:/Users/kfisher/Documents/Asia/CAMI_species/work/data/working/post-workshop/species_infra'
                            '.gdb',
                    help=u'Absolute path to workspace to hold intersected species/infrastructure feature classes.')
args = parser.parse_args()
dir_species = args.dir_species.lstrip().rstrip(' /\\')
dir_infra = args.dir_infra.lstrip().rstrip(' /\\')
dir_output = args.dir_output.lstrip().rstrip(' /\\')
dir_scratch = 'in_memory'

# dir_species = arcpy.GetParameterAsText(0)
# dir_infra = arcpy.GetParameterAsText(1)
# dir_output = arcpy.GetParameterAsText(2)
BARRIER_FIELD = 'barrier'  # not a barrier, partial barrier, complete barrier, unknown
SPECIES_FIELD = 'species'
RCTEMPLAYER = 'rc_temp'

fcs = {}
for species in conflict_matrix:
    range_fc = os.path.join(dir_species, '%s_range' % species)
    corridor_fc = os.path.join(dir_species, '%s_corridor' % species)
    rc_fc = os.path.join(dir_scratch, 'rc_fc')
    species_fc = os.path.join(dir_scratch, species)

    arcpy.Merge_management([range_fc, corridor_fc], rc_fc)
    arcpy.AddField_management(rc_fc, 'diss', 'SHORT')
    arcpy.CalculateField_management(rc_fc, 'diss', 1)
    arcpy.MakeFeatureLayer_management(rc_fc, RCTEMPLAYER)
    arcpy.Dissolve_management(RCTEMPLAYER, species_fc, 'diss', '', 'SINGLE_PART')

    for infra in conflict_matrix[species]:
        if infra not in fcs:
            fcs[infra] = []

        print('Calculating %ss for %s' % (infra, species))
        infra_fc = os.path.join(dir_infra, infra)
        infra_species_fc = os.path.join(dir_output, '%s_%s' % (infra, species))

        arcpy.Clip_analysis(infra_fc, species_fc, infra_species_fc)
        arcpy.AddField_management(infra_species_fc, BARRIER_FIELD, 'TEXT')
        # default all to 'unknown', then proceed in order of severity
        arcpy.CalculateField_management(infra_species_fc, BARRIER_FIELD, "'unknown'", 'PYTHON')
        arcpy.AddField_management(infra_species_fc, SPECIES_FIELD, 'TEXT')
        arcpy.CalculateField_management(infra_species_fc, SPECIES_FIELD, "'%s'" % species, 'PYTHON')
        fcs[infra].append(infra_species_fc)

        for level in barrier_types[1:]:
            # arcpy.SelectLayerByAttribute_management('islyr', 'CLEAR_SELECTION')
            # total = int(arcpy.GetCount_management('islyr').getOutput(0))
            if level in conflict_matrix[species][infra]:
                layer = 'islyr_%s' % level
                conditions = conflict_matrix[species][infra][level]
                condstr = ' OR '.join(["%s = '%s'" % cond for cond in conditions])
                print(condstr)
                arcpy.MakeFeatureLayer_management(infra_species_fc, layer, condstr)
                arcpy.CalculateField_management(layer, BARRIER_FIELD, "'%s'" % level, 'PYTHON')
                # arcpy.SelectLayerByAttribute_management('islyr', 'NEW_SELECTION', condstr)
                # count = int(arcpy.GetCount_management('islyr').getOutput(0))
                # print('total: %s selected: %s' % (total, count))
                # if count < total:  # no good: calc field will operate on all when really none
                #     arcpy.CalculateField_management(infra_species_fc, BARRIER_FIELD, "'%s'" % level, 'PYTHON')

print(fcs)
for infra in fcs:
    arcpy.Merge_management(fcs[infra], os.path.join(dir_output, '%s_barriers' % infra))
