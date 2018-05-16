# CAMI Atlas
Working utility scripts for Central Asian Migratory Initiative analysis and map production

## Introduction
This README provides a high-level description of the code in this repository, as well as the immediate inputs into 
and outputs from this code, delivered in a zip file via Google Drive:  
https://drive.google.com/drive/u/0/folders/1UZQ27PTKMJJH5xfy_f0fEVAX1qlDHewD  

Both the code and the data and products resulted originally from a workshop held in Vilm, Germany, April 27-30, 2017 
with 25 participants from 9 countries representing leading expertise on the 10 CMS CAMI mammals ()saiga 
antelope, Mongolian gazelle, goitered gazelle, chinkara gazelle, khulan, Bactrian camel, Bukhara deer, argali, snow 
leopard, and Asiatic cheetah) and the 5 types of linear infrastructure representing varying degrees of threat to them
 (canals, fences, pipelines, railroads, and roads). At the workshop participants edited species range/corridor data 
 and linear infrastructure data, agreed on a schema specifying which attributes (with which possible values) for each 
 type of infrastructure were necessary, assigned relative risk to each of those possible attribute values for each 
 species in a comprehensive matrix, highlighted important places where linear infrastructure represents or will 
 represent obstacles to species movements, and brainstormed a comprehensive list of possible remediation strategies 
 for these places.

Automatically generated spatial and file metadata are embedded within each dataset and are viewable via esri's 
ArcCatalog; all datasets are either use the unprojected CRS WGS84 or are projected using an Albers Equal Area 
projection suitable for North Asia ([esri id: 102025](http://epsg.io/102025)). Data may be viewed using 
the map templates described below.

## Process
At a high level, the code in this repository was used as follows.

### species_infra.py
Iterate over list of species/infrastructure threat ratings and output a feature class for each combination 
representing all infrastructure features within that species' range classified by amount of barrier. The threat 
matrix created by workshop participants (species_infrastructure_matrix (003) Mar 9.xlsx) was used to create a 
standardized hierarchical data structure stored in conflict_matrix/__init__.py as an object by species and then by 
infrastructure for use by this script. Requirements/arguments:
- arcgis workspace (geodatabase featureset or directory of shapefiles) containing a combined range/corridor feature 
class for each species
- arcgis workspace containing one feature class for each infrastructure type
- output arcgis workspace for holding calculated species/infrastructure feature classes

### species_infra_total.py
Iterate over list of species and clip the specified 'total' infrastructure by it. The output of this script was used 
to calculate approximate denominators for calculating % of total infrastructure represented by each class of threat 
for each species. Requirements/arguments:
- arcgis workspace (geodatabase featureset or directory of shapefiles) containing a combined range/corridor feature 
class for each species. Should be same as used for species_infra.py.
- infrastructure feature class (script was run once per type)
- output arcgis workspace for holding calculated species/infrastructure feature classes

### merge_species.py
Convenience script for creating polygonal species feature classes used in output maps. Script iterates over a list of
 species feature classes and adds a field with the species name to each, then merges the results. Script was run once
  for ranges and once for corridors. Requirements/arguments:
- arcgis workspace (geodatabase featureset or directory of shapefiles) containing a range/corridor feature 
class for each species
- output workspace: species.gdb/species_ranges, species.gdb/species_corridors

### output_mxd.py
An arcgis data-driven mxd was created for each infrastructure type, with pages defined by the species name in the 
species range layer. This script was used to iterate over these mxd files in a specified directory and for each one, 
programmatically advance through the 'pages' and export each one, to create the species-by-infrastructure png files 
used in the atlas.

## Data and templates
A high-level description of the datsets used by the code in this repository and delivered with the atlas 
(not part of this repository; avaialble with correct permissions at https://drive.google.com/drive/u/0/folders/1UZQ27PTKMJJH5xfy_f0fEVAX1qlDHewD) follows.

### AOI shapefiles (./context/)
- aoi_merge_project.shp -- original AOI
- aoi_analysis2.shp -- original AOI minus China and Pakistan: theoretical analysis AOI
- aoi_exclusion.shp -- part of original AOI excluded from analysis (except camel)
- aoi_plus_camel_diss.shp -- 'real' AOI encompassing species/infra features used for calculating totals

### CAMI_170927_gdb (./2017atlas/)
This esri geodatabase contains 'input' feature classes produced by editing workshop participant contributions, 
organized by species and infrastructure. Additionally, this geodatabase holds:
- conflict_feature -- expert-identified linear infrastructure segments that represent a threat to animal movement
- conflict -- conflict_feature buffered for display on maps

### species.gdb (./)
Two featuresets in this esri geodatabase, one each for species ranges and corridors, contain one feature class for each 
species; these were produced manually from source species data in CAMI_170927_gdb/species for purposes of creating 
maps as the last part of the process of processing raw participant data. The merged feature classes species_corridors
 and ranges were used in output maps (page queries show one species at a time; see above).

### species_infra.gdb (./2017atlas/)
This esri geodatabase contains the outputs of the threat calculation script (species_infra.py) detailed above:
- one feature class for each species/infra combination
- one feature class merging per species, e.g. road_barriers
In addition, this geodatabase contains a total featureset with an organization similar to that of the species/infra feature classes but calculated for a feature class designated
 as representing 'total' infrastructure of that type, e.g. all roads as determined by OSM.

### atlas_templates (./)
This directory contains the data-driven mxd files, one per infrastructure type, used by output_mxd.py to create the 
atlas pngs.

### products (./)
- 2017 CMS CAMI Data Dictionary.docx -- specification for schema used in collection of species and infrastructure 
data from workshop participants.
- CAMI possible remediation strategies.xlsx -- list generated by workshop participants
- species_infrastructure_matrix (003) Mar 9.xlsx -- matrix of the relative degree of threat posed to each species, by 
each possible value for each attribute for each type of infrastructure.
- species_by_infra -- directory of pngs produced by species_infra.py
- 170927_breakdown.xlsx -- summary linear calculations per species and infrastructure calculated from the 
linear measurements of the species/infrastructure feature classes generated by the scripts in this repository.
