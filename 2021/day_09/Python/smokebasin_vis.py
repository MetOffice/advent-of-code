import numpy as np
import imageio as ii
import smokebasin as sb

input = sb.load_input()

# greyscale for height
topography_cmap = np.linspace(0, 255, 10, dtype=np.uint8)
topography_image = topography_cmap[input]

ii.imwrite("../vis/topography.png", topography_image)

# calc low points
low_points = sb.find_low_points(input)

# topography with low points in red
low_point_image = np.stack([topography_image] * 3, axis=2)
low_point_image[low_points] = np.array([255,0,0])

ii.imwrite("../vis/low_points.png", low_point_image)

# calc basins
low_coords = sb.find_low_coords(low_points)
basin_map = sb.find_basins(input, low_coords)

# random light colours for basins, black for watersheds
basin_cmap_size = np.max(basin_map) + 1
rng  = np.random.default_rng(2022)
basin_cmap = rng.integers(64, 256, size=(basin_cmap_size, 3), dtype=np.uint8)
basin_cmap[0,:] = 0
basin_image = basin_cmap[basin_map]

ii.imwrite("../vis/basins.png", basin_image)