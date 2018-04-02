"""Basic spatial operation with shapely (buffer, union)"""
import csv
from shapely.geometry import Point, MultiPolygon
from shapely.ops import cascaded_union


def find_isolated_point(csv_path, dist):
	"""
	Determines whether a points list in a csv file has points beyond a given distance
	from the other points.

	:return: True if isolated points have been found / False otherwise
	"""
	with open(csv_path, "r") as f:
		csv_reader = csv.DictReader(f)
		buffers = [Point([float(row["x"]), float(row["y"])]).buffer(dist / 2)
				   for row in csv_reader]

	buffers_union = cascaded_union(buffers)
	if buffers_union.geom_type == "MultiPolygon":
		return True
	else:
		return False


if __name__ == "__main__":
	if find_isolated_point("data/metro_complet.csv", 500):
		print("Points isolés")
	else:
		print("Points groupés")

	if find_isolated_point("data/metro_complet.csv", 2000):
		print("Points isolés")
	else:
		print("Points groupés")
