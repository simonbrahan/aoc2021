def is_low_point(x, y, elevation):
    height = elevation[y][x]

    for neighbour_x, neighbour_y in get_neighbours(x, y, elevation):
        try:
            neighbour_height = elevation[neighbour_y][neighbour_x]
        except:
            print(neighbour_x, neighbour_y)

        if neighbour_height <= height:
            return False

    return True


def elevation_from_file(filepath):
    with open(filepath) as f:
        elevation = [[int(char) for char in line.strip()] for line in f]

    return elevation


def get_neighbours(x, y, elevation):
    directions = [(-1, 0), (0, -1), (0, 1), (1, 0)]

    out = []
    for add_x, add_y in directions:
        neighbour_x = x + add_x
        neighbour_y = y + add_y

        if 0 <= neighbour_y < len(elevation) and 0 <= neighbour_x < len(elevation[neighbour_y]):
            out.append((neighbour_x, neighbour_y))

    return out
