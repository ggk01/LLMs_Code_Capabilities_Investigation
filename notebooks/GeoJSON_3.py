# Merge all polygons and extract the outerline boundary as a Polygon,
# then save as a GeoJSON Feature containing a GeometryCollection of the outline Polygon.

import json
from shapely.geometry import shape, mapping, Polygon, MultiPolygon
from shapely.ops import unary_union

# Read the input GeoJSON file
with open('medsea_cmems_grid.json', 'r') as f:
    feature_collection = json.load(f)

# Merge all polygons into a single geometry
merged_geom = unary_union(polygons)

# Extract the outer boundary as a Polygon
if isinstance(merged_geom, Polygon):
    outline_polygon = Polygon(merged_geom.exterior)
elif isinstance(merged_geom, MultiPolygon):
    # Union all exteriors to get a single outline
    exteriors = [Polygon(p.exterior) for p in merged_geom.geoms]
    outline_union = unary_union(exteriors)
    # If the union results in a MultiPolygon, take the exterior of the unioned boundary
    if isinstance(outline_union, Polygon):
        outline_polygon = outline_union
    elif isinstance(outline_union, MultiPolygon):
        # Take the largest polygon as the outline
        outline_polygon = max(outline_union.geoms, key=lambda p: p.area)
    else:
        raise ValueError("Unexpected geometry type after union of exteriors.")
else:
    raise ValueError("Merged geometry is not a Polygon or MultiPolygon.")

# Create a GeometryCollection containing the outline Polygon
geometry_collection = {
    "type": "GeometryCollection",
    "geometries": [mapping(outline_polygon)]
}

# Wrap the GeometryCollection in a GeoJSON Feature
feature = {
    "type": "Feature",
    "geometry": geometry_collection,
    "properties": {}
}

# Save the result as a GeoJSON Feature
with open('outline_geometrycollection_feature.geojson', 'w') as out_f:
    json.dump(feature, out_f)