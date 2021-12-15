def is_low_point(x, y, elevation):
    directions = [(-1, 0), (0, -1), (0, 1), (1, 0)]

    height = elevation[y][x]

    for add_x, add_y in directions:
        neighbour_x = x + add_x
        neighbour_y = y + add_y

        if neighbour_x < 0 or neighbour_y < 0:
            continue

        try:
            neighbour_height = elevation[neighbour_y][neighbour_x]
        except IndexError:
            continue

        if neighbour_height <= height:
            return False

    return True


with open('input.txt') as f:
    elevation = [[int(char) for char in line.strip()] for line in f]

risk_level_sum = 0

for y, row in enumerate(elevation):
    for x, height in enumerate(row):
        if is_low_point(x, y, elevation):
            risk_level_sum += height + 1

print(risk_level_sum)
