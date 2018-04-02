"""Use descartes make maps with matplotlib"""
import matplotlib.pyplot as plt
from descartes.patch import Path, PathPatch
import gpxpy
from shapely.geometry import LineString


def gpx_to_shapely(gpx_path):
	"""
	Transforms a the track into a GPX file to a shapely LineString.

	:param gpx_path: full path to a GPX file
	:return: shapely LineString representing the GPS track
	"""
	gpx_file = open(gpx_path, "r")
	gpx = gpxpy.parse(gpx_file)
	points = gpx.tracks[0].segments[0].points

	coords = [[p.longitude, p.latitude] for p in points]
	return LineString(coords)


if __name__ == "__main__":
	# Parse the gpx file
	gpx_path = "data/trace.gpx"
	ls = gpx_to_shapely(gpx_path)

	# Get matplotlib current axis
	fig = plt.figure()
	ax = fig.gca()

	# Add a patch to the axis
	path = Path(ls)
	patch = PathPatch(path)
	patch.set_facecolor('none')
	ax.add_patch(patch)

	# Center the map
	ax.autoscale()
	ax.axis("equal")
	
	plt.show()
