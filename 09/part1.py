from nav import elevation_from_file, is_low_point

elevation = elevation_from_file('input.txt')

risk_level_sum = 0

for y, row in enumerate(elevation):
    for x, height in enumerate(row):
        if is_low_point(x, y, elevation):
            risk_level_sum += height + 1

print(risk_level_sum)
