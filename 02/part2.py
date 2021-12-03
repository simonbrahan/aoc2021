def line_to_instruction(line):
    direction, val = line.strip().split(' ')
    return direction, int(val)

horizontal_pos = 0
depth = 0
aim = 0

with open('input.txt') as f:
    instructions = [line_to_instruction(line) for line in f]

for direction, val in instructions:
    if direction == 'forward':
        horizontal_pos += val
        depth += aim * val

    if direction == 'up':
        aim -= val

    if direction == 'down':
        aim += val

print(horizontal_pos * depth)
