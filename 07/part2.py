def fuel_use_from_distance(distance):
    return distance * (distance + 1) / 2


with open('input.txt') as f:
    crab_positions = [int(t.strip()) for t in f.read().split(',')]

fuel_use = None
for candidate_point in range(max(crab_positions) + 1):
    candidate_fuel_use = sum(
        fuel_use_from_distance(abs(candidate_point - crab_position))
        for crab_position in crab_positions
    )

    if fuel_use is None or fuel_use > candidate_fuel_use:
        fuel_use = candidate_fuel_use

print(fuel_use)
