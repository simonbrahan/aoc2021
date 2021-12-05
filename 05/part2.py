from collections import defaultdict
import re

with open('input.txt') as f:
    lines = []
    for line in f:
        split_coords = [int(num) for num in re.split(r'\D+', line.strip())]
        coord_pairs = [(split_coords[0], split_coords[1]), (split_coords[2], split_coords[3])]
        lines.append(sorted(coord_pairs))

line_point_counts = defaultdict(int)

for line in lines:
    if line[0][0] == line[1][0]:
        points = [(line[0][0], y) for y in range(line[0][1], line[1][1] + 1)]
    elif line[0][1] == line[1][1]:
        points = [(x, line[0][1]) for x in range(line[0][0], line[1][0] + 1)]
    else:
        if line[0][0] > line[1][0]:
            xstep = -1
        else:
            xstep = 1

        if line[0][1] > line [1][1]:
            ystep = -1
        else:
            ystep = 1

        points = list(zip(range(line[0][0], line[1][0] + xstep, xstep), range(line[0][1], line[1][1] + ystep, ystep)))

    for x, y in points:
        line_point_counts[(x, y)] += 1

print(len(list(filter(lambda num: num > 1, line_point_counts.values()))))
