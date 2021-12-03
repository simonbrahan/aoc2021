def line_to_instruction(line):
    direction, distance = line.strip().split(' ')
    return direction, int(distance)

horizontal_pos = 0
depth = 0

with open('input.txt') as f:
    instructions = [line_to_instruction(line) for line in f]

for direction, distance in instructions:
    if direction == 'forward':
        horizontal_pos += distance

    if direction == 'up':
        depth -= distance

    if direction == 'down':
        depth += distance

print(horizontal_pos * depth)
