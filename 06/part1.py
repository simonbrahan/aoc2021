with open('input.txt') as f:
    fishes = [int(t.strip()) for t in f.read().split(',')]

for i in range(0, 80):
    baby_count = 0
    for idx, _ in enumerate(fishes):
        fishes[idx] -= 1
        if fishes[idx] < 0:
            fishes[idx] = 6
            baby_count += 1

    fishes.extend([8] * baby_count)

print(len(fishes))
