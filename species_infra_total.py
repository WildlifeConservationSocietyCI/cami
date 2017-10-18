import os
import argparse
from argparse import RawDescriptionHelpFormatter
import arcpy
from arcpy import env
from conflict_matrix import *

env.overwriteOutput = True

parser = argparse.ArgumentParser(description=u"""
Iterate over list of species and clip the specified 'total' infrastructure by it.
""",
                                 formatter_class=RawDescriptionHelpFormatter)
parser.add_argument('-s', '--dir_species',
                    default='C:/Users/kfisher/Documents/Asia/CAMI_species/work/data/working/post-workshop/2017atlas'
                            '/CAMI_170927.gdb/species',
                    help=u'Absolute path to workspace containing species feature classes.')
parser.add_argument('-i', '--infra_fc',
                    # default='C:/Users/kfisher/Documents/Asia/CAMI_species/work/data/working/post-workshop/2017atlas'
                    #         '/CAMI_170927.gdb/infrastructure/road_total',
                    # default='C:/Users/kfisher/Documents/Asia/CAMI_species/work/data/working/post-workshop/2017atlas'
                    #         '/CAMI_170927.gdb/infrastructure/railroad_total',
                    # default='C:/Users/kfisher/Documents/Asia/CAMI_species/work/data/working/post-workshop/2017atlas'
                    #         '/CAMI_170927.gdb/infrastructure/fence',
                    default='C:/Users/kfisher/Documents/Asia/CAMI_species/work/data/working/post-workshop/2017atlas'
                            '/CAMI_170927.gdb/infrastructure/pipeline',
                    help=u'Absolute path to infrastructure feature class to be clipped.')
parser.add_argument('-o', '--dir_output',
                    default='C:/Users/kfisher/Documents/Asia/CAMI_species/work/data/working/post-workshop/2017atlas'
                            '/species_infra.gdb/total',
                    help=u'Absolute path to workspace to hold intersected species/infrastructure feature classes.')
args = parser.parse_args()
dir_species = args.dir_species.lstrip().rstrip(' /\\')
infra_fc = args.infra_fc.lstrip().rstrip(' /\\')
infra = infra_fc.split('/')[-1].split('.')[0]
dir_output = args.dir_output.lstrip().rstrip(' /\\')
dir_scratch = 'C:/Users/kfisher/Documents/Asia/CAMI_species/work/data/working/post-workshop/2017atlas' \
              '/species_infra.gdb/scratch'  # 'in_memory'

SPECIES_FIELD = 'species'
RCTEMPLAYER = 'rc_temp'

fcs = {}
for species in conflict_matrix:
    print('Calculating %s for %s' % (infra, species))
    if infra not in fcs:
        fcs[infra] = []
    range_fc = os.path.join(dir_species, '%s_range' % species)
    corridor_fc = os.path.join(dir_species, '%s_corridor' % species)
    rc_fc = os.path.join(dir_scratch, 'rc_fc')
    species_fc = os.path.join(dir_scratch, species)

    arcpy.Merge_management([range_fc, corridor_fc], rc_fc)
    arcpy.AddField_management(rc_fc, 'diss', 'SHORT')
    arcpy.CalculateField_management(rc_fc, 'diss', 1)
    arcpy.MakeFeatureLayer_management(rc_fc, RCTEMPLAYER)
    arcpy.Dissolve_management(RCTEMPLAYER, species_fc, 'diss', '', 'SINGLE_PART')

    infra_species_fc = os.path.join(dir_output, '%s_total_%s' % (infra, species))
    arcpy.Clip_analysis(infra_fc, species_fc, infra_species_fc)
    arcpy.AddField_management(infra_species_fc, SPECIES_FIELD, 'TEXT')
    arcpy.CalculateField_management(infra_species_fc, SPECIES_FIELD, "'%s'" % species, 'PYTHON')
    fcs[infra].append(infra_species_fc)

print(fcs)
for infra in fcs:
    arcpy.Merge_management(fcs[infra], os.path.join(dir_output, '%s_by_species' % infra))
