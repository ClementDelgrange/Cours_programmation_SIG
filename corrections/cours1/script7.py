"""Use folium to make dynamic maps"""
import folium, folium.plugins
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

	coords = [[p.latitude, p.longitude] for p in points]
	return LineString(coords)


if __name__ == "__main__":
    # Parse the gpx file
    gpx_path = "data/trace.gpx"
    ls = gpx_to_shapely(gpx_path)

    # Compute the map center
    ave_lat, ave_lon = ls.centroid.x, ls.centroid.y

    # Define the map
    ma_carte = folium.Map(location=[ave_lat, ave_lon], zoom_start=13)

    # Add the linestring
    polyline = folium.PolyLine(ls.coords, color='purple', weight=5).add_to(ma_carte)

    # Add a symbology to the linestring
    attr = {"fill": "black", "font-size": "48"}
    folium.plugins.PolyLineTextPath(polyline,
                                 "      >      ",
                                 repeat=True,
                                 offset=18,
                                 attributes=attr).add_to(ma_carte)

    # Save the map in a html file
    ma_carte.save("data/ma_carte.html")
