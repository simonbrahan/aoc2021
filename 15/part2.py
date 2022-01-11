from dijkstra import get_risk
from math import floor

def translate_risk(risk, x, y, tile_width, tile_height):
    x_translation = floor(x / tile_width)
    y_translation = floor(y / tile_height)

    risk_translation = (risk + x_translation + y_translation -1) % 9 + 1

    return risk_translation


with open('input.txt') as f:
    grid_tile = [[int(risk) for risk in line.strip()] for line in f]

tile_width = len(grid_tile[0])
full_width = tile_width * 5
tile_height = len(grid_tile)
full_height = tile_height* 5

full_grid = [[] for y in range(full_height)]

for y in range(full_height):
    for x in range(full_width):
        full_grid[y].append(translate_risk(grid_tile[y%tile_height][x%tile_width], x, y, tile_width, tile_height))

print(get_risk(full_grid))
