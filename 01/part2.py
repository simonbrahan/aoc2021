from collections import deque
import math

with open('input.txt') as f:
    readings = [int(line.strip()) for line in f]

# use infinity here to simplify first check
last_window_sum = math.inf

window = deque(maxlen = 3)

increase_count = 0

for reading in readings:
    window.append(reading)

    if len(window) < 3:
        continue

    new_window_sum = sum(window)

    if new_window_sum > last_window_sum:
        increase_count += 1

    last_window_sum = new_window_sum

print(increase_count)
