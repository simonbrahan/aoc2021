from collections import Counter, defaultdict

def update_polymer(polymer, rules):
    new_polymer = ''
    for i in range(len(polymer) - 1):
        new_polymer += polymer[i]
        if rules[polymer[i]][polymer[i+1]]:
            new_polymer += rules[polymer[i]][polymer[i+1]]

    new_polymer += polymer[-1]

    return new_polymer


with open('input.txt') as f:
    polymer = f.readline().strip()
    next(f)
    pair_insertion_rules = defaultdict(lambda: defaultdict(str))
    for line in f:
        matches, new_letter = line.strip().split(' -> ')
        pair_insertion_rules[matches[0]][matches[1]] = new_letter

for i in range(10):
    polymer = update_polymer(polymer, pair_insertion_rules)

char_counts = Counter(polymer).values()

print(max(char_counts) - min(char_counts))
