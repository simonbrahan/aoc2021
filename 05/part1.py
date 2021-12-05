from collections import defaultdict
import re

with open('input.txt') as f:
    lines = []
    for line in f:
        split_coords = [int(num) for num in re.split(r'\D+', line.strip())]
        coord_pairs = [(split_coords[0], split_coords[1]), (split_coords[2], split_coords[3])]

        if coord_pairs[0][0] == coord_pairs[1][0] or coord_pairs[0][1] == coord_pairs[1][1]:
            lines.append(sorted(coord_pairs))

line_point_counts = defaultdict(int)

for line in lines:
    for x in range(line[0][0], line[1][0] + 1):
        for y in range(line[0][1], line[1][1] + 1):
            line_point_counts[(x, y)] += 1

print(len(list(filter(lambda num: num > 1, line_point_counts.values()))))
