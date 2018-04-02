import gpxpy
from shapely.geometry import LineString
import json


def gpx_to_shapely(gpx_path):
	"""
	Transforms a the track into a GPX file to a shapely LineString.
	"""
	gpx_file = open(gpx_path, "r")
	gpx = gpxpy.parse(gpx_file)
	points = gpx.tracks[0].segments[0].points

	coords = [[p.longitude, p.latitude, p.elevation] for p in points]
	return LineString(coords)


def shapely_to_geojson(ls, geojson_path):
	"""
	Write a GeoJSON file with the input shapely geometry.
	"""
	geojson = ls.__geo_interface__
	with open(geojson_path, "w") as f:
		f.write(json.dumps(geojson))


if __name__ == "__main__":
	gpx_path = "data/trace.gpx"
	geojson_path = "data/trace.geojson"
	ls = gpx_to_shapely(gpx_path)
	shapely_to_geojson(ls, geojson_path)
