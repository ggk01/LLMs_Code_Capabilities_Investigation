import json
from shapely.geometry import mapping

# Create a GeometryCollection of Polygon geometries from exteriors
geometry_collection = {
    "type": "GeometryCollection",
    "geometries": [mapping(polygon) for polygon in exteriors]
}

# Wrap the GeometryCollection in a GeoJSON Feature
feature = {
    "type": "Feature",
    "geometry": geometry_collection,
    "properties": {}
}

# Save the result as a GeoJSON Feature
with open('grids_outerline_geometrycollection_feature.geojson', 'w') as f:
    json.dump(feature, f)