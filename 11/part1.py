def get_neighbours(x, y, squids):
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

    out = []
    for add_x, add_y in directions:
        neighbour_x = x + add_x
        neighbour_y = y + add_y

        if 0 <= neighbour_y < len(squids) and 0 <= neighbour_x < len(squids[neighbour_y]):
            out.append((neighbour_x, neighbour_y))

    return out


def maybe_flash(x, y, squids, flashed_squids):

    if squids[y][x] <= 9 or (x, y) in flashed_squids:
        return squids, flashed_squids

    flashed_squids.add((x, y))

    neighbours = get_neighbours(x, y, squids)

    for neighbour_x, neighbour_y in neighbours:
        squids[neighbour_y][neighbour_x] += 1
        squids, flashed_squids = maybe_flash(neighbour_x, neighbour_y, squids, flashed_squids)

    return squids, flashed_squids


with open('input.txt') as f:
    squids = [[int(level) for level in row.strip()] for row in f]

total_flashes = 0
for i in range(100):
    squids = [[level + 1 for level in row] for row in squids]

    flashed_squids = set()
    for y, row in enumerate(squids):
        for x, level in enumerate(row):
            squids, flashed_squids = maybe_flash(x, y, squids, flashed_squids)

    squids = [[0 if level > 9 else level for level in row] for row in squids]

    total_flashes += len(flashed_squids)

print(total_flashes)
