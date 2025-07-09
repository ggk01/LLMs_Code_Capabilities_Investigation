import json
from shapely.geometry import shape, mapping, Polygon, MultiPolygon
from shapely.ops import unary_union

# Read the input GeoJSON file
with open('medsea_cmems_grid.json', 'r') as f:
    feature_collection = json.load(f)
    
# Merge all polygons in the FeatureCollection and extract the outer boundary as a single Polygon

# Extract polygons from the FeatureCollection
polygons = []
for feature in feature_collection['features']:
    geom = shape(feature['geometry'])
    if isinstance(geom, Polygon):
        polygons.append(geom)
    elif isinstance(geom, MultiPolygon):
        polygons.extend(list(geom.geoms))

# Union all polygons
merged = unary_union(polygons)

# Extract the exterior boundary as a Polygon
if isinstance(merged, Polygon):
    outline = Polygon(merged.exterior)
elif isinstance(merged, MultiPolygon):
    # Take the exterior of the unioned MultiPolygon as a single boundary
    merged_union = unary_union([Polygon(p.exterior) for p in merged.geoms])
    outline = Polygon(merged_union.exterior)
else:
    raise ValueError("Union did not result in a Polygon or MultiPolygon.")

# Prepare GeoJSON output
outline_geojson = {
    "type": "Feature",
    "geometry": mapping(outline),
    "properties": {}
}

# Save the result as a GeoJSON file
with open('merged_outline.geojson', 'w') as out_f:
    json.dump(outline_geojson, out_f)