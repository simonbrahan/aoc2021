from squids import maybe_flash

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
