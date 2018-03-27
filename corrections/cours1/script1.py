from shapely.geometry import Point, Polygon
from shapely.validation import explain_validity


def points_to_polygon(points):
	"""
	Transform a shapely point list in a shapely polygon.

	:param points: list of shapely.geometry.Point
	:return: a shapely.geometry.Polygon
	"""
	coords = []
	for point in points:
		coords.append(list(point.coords)[0])
	poly = Polygon(coords)
	return poly


def get_polygon_validity(points):
	"""
	Checks if the points list make a valid polygon,
	and determines the invalidity reason if the polygon isn't valid.

	:param points: list of shapely.geometry.Point
	:return:
		- (True, "")  is the polygon is valid
		- (False, "<invalidity reason>") is the polygon isn't valid
	"""
	poly = points_to_polygon(points)
	if poly.is_valid:
		return True, ""
	else:
		return False, explain_validity(poly)


if __name__ == "__main__":
	p1 = Point([0, 0])
	p2 = Point([0, 5])
	p3 = Point([5, 0])
	p4 = Point([5, 5])
	p5 = Point([0, 0])
	points = [p1, p2, p3, p4, p5]
	print(get_polygon_validity(points))

	p1 = Point([0, 0])
	p2 = Point([0, 5])
	p3 = Point([5, 5])
	p4 = Point([5, 0])
	p5 = Point([0, 0])
	points = [p1, p2, p3, p4, p5]
	print(get_polygon_validity(points))
