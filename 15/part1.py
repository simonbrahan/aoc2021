from collections import defaultdict
import math

def get_neighbours(cell, grid):
    x, y = cell
    directions = [(-1, 0), (0, -1), (0, 1), (1, 0)]

    out = []
    for add_x, add_y in directions:
        neighbour_x = x + add_x
        neighbour_y = y + add_y

        if 0 <= neighbour_y < len(grid) and 0 <= neighbour_x < len(grid[neighbour_y]):
            out.append((neighbour_x, neighbour_y))

    return out


with open('input.txt') as f:
    grid = [[int(risk) for risk in line.strip()] for line in f]

destination = (len(grid) - 1, len(grid[0]) - 1)
cumulative_cell_risks = defaultdict(lambda: math.inf)
cumulative_cell_risks[(0, 0)] = 0

unvisited_cells = set()
for y, row in enumerate(grid):
    for x, cell in enumerate(row):
        unvisited_cells.add((x, y))

while destination in unvisited_cells:
    current = min(unvisited_cells, key=lambda cell: cumulative_cell_risks[cell])
    neighbours = get_neighbours(current, grid)

    for neighbour in neighbours:
        if neighbour not in unvisited_cells:
            continue

        neighbour_risk = min(
            cumulative_cell_risks[neighbour],
            cumulative_cell_risks[current] + grid[neighbour[1]][neighbour[0]]
        )

        cumulative_cell_risks[neighbour] = neighbour_risk

    unvisited_cells.remove(current)

for y in range(11):
    row = []
    for x in range(11):
        risk = cumulative_cell_risks[(x, y)]

        if risk == math.inf:
            row.append('  ')
        else:
            row.append('%2d' % risk)

    print(' '.join(row))

print(cumulative_cell_risks[destination])
