import json
from shapely.geometry import shape, mapping, Polygon, MultiPolygon
from shapely.ops import unary_union

def featurecollection_to_outline_geometrycollection(feature_collection):
    # Extract polygons from the FeatureCollection
    polygons = []
    for feature in feature_collection['features']:
        geom = shape(feature['geometry'])
        if isinstance(geom, Polygon):
            polygons.append(geom)
        elif isinstance(geom, MultiPolygon):
            polygons.extend(list(geom.geoms))
    # Union all polygons to get the combined outline
    unioned = unary_union(polygons)
    # Get the exterior boundary as a closed Polygon
    if isinstance(unioned, (Polygon, MultiPolygon)):
        outline = Polygon(unioned.exterior)
    else:
        raise ValueError("Union did not result in a Polygon or MultiPolygon.")
    # Create a GeometryCollection with the outline polygon
    geometry_collection = {
        "type": "GeometryCollection",
        "geometries": [mapping(outline)]
    }
    return geometry_collection

# Read the input GeoJSON file
with open('medsea_cmems_grid.json', 'r') as f:
    feature_collection = json.load(f)

# Get the outline geometry collection
geometry_collection = featurecollection_to_outline_geometrycollection(feature_collection)

# Save the result as a GeoJSON file
with open('outline_geometrycollection.geojson', 'w') as f:
    json.dump(geometry_collection, f)