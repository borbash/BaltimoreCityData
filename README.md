BaltimoreCityData
=================

The file cameras2.json has Baltimore City's crime cameras, those that blink blue and reside atop telephone poles overlooking intersections usually. 

The file Baltimore_Fixed_Speed_Cameras is a geojson of Baltimore's eighty speed/traffic cameras. 

Both are derived from CSVs downloaded from Baltimore City's open gov site. Used pyshp and json packages in python to manipulate the city data into geojson format.

The python script uploads a bunch (eighty) of changes to OpenStreetMap based on the content of the geojson file. It makes use of the helpful osmapi package at https://github.com/metaodi/osmapi. Note that before adding these camera locations, I was careful to check that these speed cameras weren't already on the OSM map. (To do that, I got overpass's .osm file for Baltimore and found that it contained no string "speed_camera") Adding duplicates to OSM would not be nice.

