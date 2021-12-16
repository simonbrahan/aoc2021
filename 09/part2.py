from math import prod
from nav import elevation_from_file, get_basin_size, is_low_point

elevation = elevation_from_file('input.txt')

basin_sizes = []

for y, row in enumerate(elevation):
    for x, height in enumerate(row):
        if is_low_point(x, y, elevation):
            basin_sizes.append(get_basin_size(x, y, elevation))

print(prod(sorted(basin_sizes)[-3:]))
