"""Intersect linestring and plot the result in matplotlib"""
from shapely.geometry import LineString, Point, MultiPoint
import matplotlib.pyplot as plt


def plot_linestring(ls):
	"""
	Draw a shapely LineString into a matplotlib graphic.
	"""
	xx = ls.xy[0]
	yy = ls.xy[1]
	plt.plot(xx, yy, "-b")


def plot_point(pt):
	"""
	Draw a shapely Point or MultiPoint into a matplotlib graphic.
	"""
	if pt.geom_type == "MultiPoint":
		for geom in pt.geoms:
			plot_point(geom)
	elif pt.geom_type == "Point":
		c = pt.xy
		plt.plot(c[0], c[1], "ro")
	else:
		print("cas non traité")


def plot_linestring_intersection(ls1, ls2):
	"""
	Draw two shapely LineString and their intersection into a matplotlib graphic.
	"""
	pt = l1.intersection(l2)
	plot_linestring(l1)
	plot_linestring(l2)
	plot_point(pt)
	plt.show()


if __name__ == "__main__":
	l1 = LineString([[0, 0], [1, 1], [2, 0]])
	l2 = LineString([[0, 0.5], [2, 0.5]])
	plot_linestring_intersection(l1, l2)
