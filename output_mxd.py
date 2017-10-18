import os
import arcpy

field_name = 'species'
dir_mxd = 'C:/Users/kfisher/Documents/Asia/CAMI_species/work/maps/atlas_templates'
dir_output = 'C:/Users/kfisher/Documents/Asia/CAMI_species/work/maps/species_by_infra'
NOTE_SPECIES = [u'Ovis ammon', u'Panthera uncia']
SHOW_EXCLUDED_AREA_SPECIES = [u'Camelus bactrianus']
INFRA_TOTALS = {u'canal': u'canal',
                u'fence': u'fence',
                u'pipeline': u'pipeline',
                u'railroad': u'OSM railroad',
                u'road': u'OSM road'
                }
INFRA_NOTE_X_ON = 4.24
INFRA_NOTE_X_OFF = 12

for filename in os.listdir(dir_mxd):
    fullpath = os.path.join(dir_mxd, filename)
    if os.path.isfile(fullpath):
        basename, extension = os.path.splitext(fullpath)
        if extension.lower() == ".mxd":
            series = os.path.split(basename)[-1]
            print('Exporting %s' % series)
            filebasename = series.rsplit('_', 1)[0]
            infra = series.split('_')[0]
            infra_total_layername = INFRA_TOTALS[infra]
            mxd = arcpy.mapping.MapDocument(fullpath)
            df = arcpy.mapping.ListDataFrames(mxd, 'Layers')[0]

            for i in range(1, mxd.dataDrivenPages.pageCount + 1):
                mxd.dataDrivenPages.currentPageID = i
                row = mxd.dataDrivenPages.pageRow
                species = row.getValue(field_name)
                pageName = species.replace(' ', '_')
                print('Page: %s' % pageName)

                # if species name is argali or SL, show infra_note; else, hide it
                infra_note = arcpy.mapping.ListLayoutElements(mxd, 'TEXT_ELEMENT', 'infra_note')[0]
                infra_note.elementPositionX = INFRA_NOTE_X_OFF
                if species in NOTE_SPECIES:
                    infra_note.elementPositionX = INFRA_NOTE_X_ON

                # if species is camel, show excluded countries
                excl = arcpy.mapping.ListLayers(mxd, 'aoi_exclusion', df)[0]
                excl.visible = True
                infra_total, infra_total_full = arcpy.mapping.ListLayers(mxd, infra_total_layername, df)
                infra_total.visible = True
                infra_total_full.visible = False
                if species in SHOW_EXCLUDED_AREA_SPECIES:
                    excl.visible = False
                    infra_total.visible = False
                    infra_total_full.visible = True

                outfile = os.path.join(dir_output, '%s_%s.png' % (filebasename, pageName))
                arcpy.mapping.ExportToPNG(mxd, outfile, resolution=300)

            del mxd  # deletes reference, not file
