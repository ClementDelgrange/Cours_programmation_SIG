"""Mask the area outside of the input polygons"""
import rasterio
from rasterio.tools.mask import mask
import fiona
from fiona.transform import transform_geom


def build_mask(raster_path, shp_path, dest_path):
    # Read the GeoTIFF with rasterio
    with rasterio.open(raster_path) as src:
        profile = src.profile
        crs = profile["crs"].to_string()

        # Read the shapefile with fiona
        with fiona.open(shp_path, "r") as shapefile:
            shp_crs = shapefile.crs
            geoms = [transform_geom(shapefile.crs, crs, feature["geometry"]) for feature in shapefile]

        # Mask with the list of geometries; crop to the geoms extent
        dest_image, dest_transform = mask(src, geoms, crop=True)


    # Update the profile
    profile["height"] = dest_image.shape[1]
    profile["width"] = dest_image.shape[2]
    profile["transform"] = dest_transform

    # Write the masked data in the destination raster
    with rasterio.open(dest_path, "w", **profile) as dest:
        dest.write(dest_image)


if __name__ == "__main__":
    build_mask("data/dsm.tif", "data/stocks.shp", "data/output.tif")
