"""Reproject GeoJSON geometries"""
from pyproj import transform, Proj
from shapely.geometry import Polygon, shape, mapping
from shapely.wkt import loads


def transform_geom(geom, in_epsg, out_epsg):
    """
    Transform a geometry from one reference system to another.

    :param geom: a GeoJSON geometry with `type` and `coordinates` members
    :param in_crs: a string like 'EPSG:4326' representing the coordinate reference system of the input geometry
    :param out_crs: a string like 'EPSG:4326' representing the coordinate reference system of the input geometry
    :return: the transformed GeoJSON geometry
    """
    in_crs = Proj(init=in_epsg)
    out_crs = Proj(init=out_epsg)

    if geom["type"] == "Point":
        xi, yi = geom["coordinates"]
        xf, yf = transform(in_crs, out_crs, xi, yi)
        geom["coordinates"] = [xf, yf]

    elif geom["type"] in ["LineString", "MultiPoint"]:
        xi, yi = zip(*geom["coordinates"])
        xf, yf = transform(in_crs, out_crs, xi, yi)
        geom["coordinates"] = [xf, yf]

    elif geom["type"] in ["Polygon", "MultiLineString"]:
        new_rings = []
        for ring in geom["coordinates"]:
            xi, yi = zip(*ring)
            xf, yf = transform(in_crs, out_crs, xi, yi)
            new_rings.append(list(zip(xf, yf)))

        geom["coordinates"] = new_rings

    elif geom["type"] == "MultiPolygon":
        new_parts = []
        for part in geom["coordinates"]:
            new_rings = []
            for ring in part:
                xi, yi = zip(*ring)
                xf, yf = transform(in_crs, out_crs, xi, yi)
                new_rings.append(list(zip(xf, yf)))
            new_parts.append(new_rings)

        geom["coordinates"] = new_parts

    elif geom["type"] == "FeatureCollection":
        for feature in geom["Features"]:
            transform_geom(feature["geometry"], in_epsg, out_epsg)

    else:
        raise ValueError(f"{geom['type']} isn't a valid geometry type")


if __name__ == "__main__":
    # Load the WKT in shapely
    wkt = "POLYGON ((25.80954551696777 66.55355747998166, 25.85220336914062 66.57588240547837, 25.85108757019043 66.57622360944596, 25.808687210083 66.55386483992372, 25.80954551696777 66.55355747998166))"
    poly = loads(wkt)

    # Get the __geo_interface__ and transform coordinates in UTM 35N
    geojson = mapping(poly)
    transform_geom(geojson, "EPSG:4326", "EPSG:32635")
    poly_utm = shape(geojson)
    print(poly_utm.area)  # 177328.246773921

    # Get the __geo_interface__ and transform coordinates in Pseudo Mercator
    geojson = mapping(poly)
    transform_geom(geojson, "EPSG:4326", "EPSG:3857")
    poly_pseudo_merc = shape(geojson)
    print(poly_pseudo_merc.area)  # 1116853.1942340452

    # Both UTM and Pseudo Mercator are "non equal area" projections.
    # So the two results are false, but this one in UTM should be closer to the reality (less distortion with this projection).
