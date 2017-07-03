import os
import arcpy

field_name = 'species'
dir_mxd = 'C:/Users/kfisher/Documents/Asia/CAMI_species/work/maps/atlas_templates'
dir_output = 'C:/Users/kfisher/Documents/Asia/CAMI_species/work/maps/species_by_infra'

for filename in os.listdir(dir_mxd):
    fullpath = os.path.join(dir_mxd, filename)
    if os.path.isfile(fullpath):
        basename, extension = os.path.splitext(fullpath)
        if extension.lower() == ".mxd":
            series = os.path.split(basename)[-1]
            print('Exporting %s' % series)
            filebasename = series.rsplit('_', 1)[0]
            mxd = arcpy.mapping.MapDocument(fullpath)
            for i in range(1, mxd.dataDrivenPages.pageCount + 1):
                mxd.dataDrivenPages.currentPageID = i
                row = mxd.dataDrivenPages.pageRow
                pageName = row.getValue(field_name).replace(' ', '_')
                print('Page: %s' % pageName)
                outfile = os.path.join(dir_output, '%s_%s.png' % (filebasename, pageName))
                arcpy.mapping.ExportToPNG(mxd, outfile)
            del mxd
