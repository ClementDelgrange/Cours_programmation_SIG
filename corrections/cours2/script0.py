"""Read and write a raster with rasterio"""
import rasterio
import numpy as np
from pprint import pprint  # pprint for pretty printing


# Read an ortho
ortho_path = "data/ortho_32.00cm.tif"
with rasterio.open(ortho_path) as src:
	data = src.read()
	profile = src.profile
	bounds = src.bounds

# Print metadata
pprint(profile)
pprint(bounds)

# Extract only one band
band = data[0]
profile["count"] = 1

# Write extracted band into a new raster
out_path = "data/output.tif"
with rasterio.open(out_path, "w", **profile) as dest:
	dest.write(band, 1)
