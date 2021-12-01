with open('sample.txt') as f:
    readings = [int(line.strip()) for line in f]

last_reading = None

increase_count = 0

for reading in readings:
    if last_reading is not None and reading > last_reading:
        increase_count += 1

    last_reading = reading

print(increase_count)
