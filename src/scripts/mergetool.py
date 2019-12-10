import json
import geojson
from functools import partial
import pyproj
import shapely.geometry
import shapely.ops
import sys

if len(sys.argv) != 4:
    print("Input in form: python mergetool <file1.json> <file2.json> <Merged.json>")
    sys.exit()

# reading into two geojson objects, in a GCS (WGS84)
path = "../../assets/county/"
path2 = "../../assets/1950/metro/"
f1 = path + sys.argv[1]
f2 = path + sys.argv[2]
f3 = path2 + sys.argv[3]
with open(f1) as geojson1:
    poly1_geojson = json.load(geojson1)

with open(f2) as geojson2:
    poly2_geojson = json.load(geojson2)


# pulling out the polygons

poly1 = shapely.geometry.asShape(poly1_geojson['features'][0]['geometry'])
poly2 = shapely.geometry.asShape(poly2_geojson['features'][0]['geometry'])

# checking to make sure they registered as polygons
print(poly1.geom_type)
print(poly2.geom_type)

# merging the polygons - they are feature collections, containing a point, a polyline, and a polygon - I extract the polygon
# for my purposes, they overlap, so merging produces a single polygon rather than a list of polygons
mergedPolygon = poly1.union(poly2)

# using geojson module to convert from WKT back into GeoJSON format
geojson_out = geojson.Feature(geometry=mergedPolygon, properties={})

# outputting the updated geojson file - for mapping/storage in its GCS format
with open(f3, 'w') as outfile:
    json.dump(geojson_out.geometry, outfile)
outfile.close()

# reprojecting the merged polygon to determine the correct area
# it is a polygon covering much of the US, and dervied form USGS data, so using Albers Equal Area
project = partial(
    pyproj.transform,
    pyproj.Proj(init='epsg:4326'),
    pyproj.Proj(init='epsg:5070'))

mergedPolygon_proj = shapely.ops.transform(project,mergedPolygon)
