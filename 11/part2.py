from squids import maybe_flash

with open('input.txt') as f:
    squids = [[int(level) for level in row.strip()] for row in f]
    total_squids = len(squids) * len(squids[0])

steps = 0
flashed_squids_count = 0
while flashed_squids_count != total_squids:
    steps += 1

    squids = [[level + 1 for level in row] for row in squids]

    flashed_squids = set()
    for y, row in enumerate(squids):
        for x, level in enumerate(row):
            squids, flashed_squids = maybe_flash(x, y, squids, flashed_squids)

    squids = [[0 if level > 9 else level for level in row] for row in squids]

    flashed_squids_count = len(flashed_squids)

print(steps)
