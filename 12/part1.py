from collections import defaultdict

small_caves = set()
links = defaultdict(list)
with open('input.txt') as f:
    for line in f:
        left, right = line.strip().split('-')

        links[left].append(right)
        links[right].append(left)

        if left.islower():
            small_caves.add(left)
        if right.islower():
            small_caves.add(right)

paths = [['start']]
complete_paths = []
while len(paths) > 0:
    path = paths.pop(0)
    current_cave = path[-1]

    # If we're in the end cave, add this to the complete paths and skip to the next path
    if current_cave == 'end':
        complete_paths.append(path)
        continue

    options = links[current_cave]
    for option in options:
        # If this option is a small cave and we've already been in it, skip to the next option
        if option in path and option in small_caves:
            continue

        paths.append(path + [option])

print(len(complete_paths))
