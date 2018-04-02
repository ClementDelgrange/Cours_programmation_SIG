"""Make a mask on a raster with rasterio"""
import rasterio


# Read input raster
with rasterio.open("data/ortho_32.00cm.tif") as src:
    r, g, b, a = src.read()
    profile = src.profile

# Build the mask
tot = r + g + b
tot[tot > 200] = 255
tot[tot <= 200] = 0

# There is only one band in the output
profile["count"] = 1

# Write output raster
with rasterio.open("data/output.tif", "w", **profile) as dest:
    dest.write(tot, 1)
