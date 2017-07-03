import os
import argparse
from argparse import RawDescriptionHelpFormatter
import arcpy
from arcpy import env

env.overwriteOutput = True

parser = argparse.ArgumentParser(description=u"""
Iterate over list of species fcs and add field with species name to each, then merge.
""",
                                 formatter_class=RawDescriptionHelpFormatter)
parser.add_argument('-s', '--dir_species',
                    default='C:/Users/kfisher/Documents/Asia/CAMI_species/work/data/working/post-workshop/species'
                            '.gdb/corridors',
                    help=u'Absolute path to workspace containing species feature classes.')
parser.add_argument('-o', '--dir_output',
                    default='C:/Users/kfisher/Documents/Asia/CAMI_species/work/data/working/post-workshop/species.gdb',
                    help=u'Absolute path to workspace to hold output.')
args = parser.parse_args()
dir_species = args.dir_species.lstrip().rstrip(' /\\')
dir_output = args.dir_output.lstrip().rstrip(' /\\')
dir_scratch = 'in_memory'

SPECIES_FIELD = 'species'
RCTEMPLAYER = 'rc_temp'

arcpy.env.workspace = dir_species
species_ranges = arcpy.ListFeatureClasses()
for s in species_ranges:
    species_name = s.replace('_', ' ')[:-9]
    print species_name
    arcpy.AddField_management(s, SPECIES_FIELD, 'TEXT')
    arcpy.CalculateField_management(s, SPECIES_FIELD, '"%s"' % species_name, 'PYTHON_9.3')

arcpy.Merge_management(species_ranges, os.path.join(dir_output, 'species_corridors'))
