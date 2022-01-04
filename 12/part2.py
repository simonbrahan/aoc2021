from collections import defaultdict
from copy import copy

small_caves = set()
links = defaultdict(list)
with open('sample.txt') as f:
    for line in f:
        left, right = line.strip().split('-')

        if right != 'start':
            links[left].append(right)
        if left != 'start':
            links[right].append(left)

        if left.islower():
            small_caves.add(left)
        if right.islower():
            small_caves.add(right)

paths = [(['start'], defaultdict(int))]
complete_paths = []
while len(paths) > 0:
    path, cave_visit_count = paths.pop(0)
    current_cave = path[-1]

    # If we're in the end cave, add this to the complete paths and skip to the next path
    if current_cave == 'end':
        print(','.join(path))
        complete_paths.append(path)
        continue

    new_cave_visit_count = copy(cave_visit_count)
    # If this option is a small cave, check whether we're allowed to visit it again
    if current_cave in small_caves:
        # If we've visited this cave twice, no go
        if cave_visit_count[current_cave] == 2:
            continue

        # If we've visited this cave once and ANY small cave twice, no go
        if cave_visit_count[current_cave] == 1 and 2 in cave_visit_count.values():
            continue

        new_cave_visit_count[current_cave] += 1

    options = links[current_cave]
    for option in options:
        paths.append((path + [option], new_cave_visit_count))

print(len(complete_paths))
