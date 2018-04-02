"""Reproject raster"""
import rasterio
from rasterio.warp import calculate_default_transform, reproject


def create_ortho_mask(in_path, dst_path, dst_crs=None):
    """Create a mask on an orthophotography and write the output in the specified crs"""
    # Read the input raster
    with rasterio.open(in_path) as src:
        r, g, b, a = src.read()
        profile = src.profile
        bounds = src.bounds

    # Build the mask
    tot = r + g + b
    tot[tot > 200] = 255
    tot[tot <= 200] = 0

    # There is only one band in the output
    profile["count"] = 1

    # If dst_crs is define, we transform the raster to the destination crs
    if dst_crs:
        # Calculate the ideal dimensions and transformation in the new crs
        dst_affine, dst_width, dst_height = calculate_default_transform(
            profile["crs"], dst_crs, profile["width"], profile["height"], *bounds)

        # Update the profile
        profile['crs'] = dst_crs
        profile['transform'] = dst_affine
        profile['affine'] = dst_affine
        profile['width'] = dst_width
        profile['height'] = dst_height

        # Reproject with the default resampling method
        reproject(
            source=tot,
            src_crs=profile["crs"],
            src_transform=profile["affine"],
            destination=tot,
            dst_transform=dst_affine,
            dst_crs=dst_crs)

    # Write the output raster
    with rasterio.open(dst_path, "w", **profile) as dest:
        dest.write(tot, 1)


if __name__ == "__main__":
    create_ortho_mask("data/ortho_32.00cm.tif", "data/output.tif")
    create_ortho_mask("data/ortho_32.00cm.tif", "data/output_EPSG_3857.tif", "EPSG:3857")
