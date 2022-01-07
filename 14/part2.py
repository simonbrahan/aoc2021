from collections import defaultdict, Counter
from itertools import pairwise

def pair_counts(polymer):
    return Counter(map(lambda pair: ''.join(pair), pairwise(polymer)))


def update_pair_counts(pair_counts, rules):
    new_counts = defaultdict(int)

    for pair, count in pair_counts.items():
        for pair in rules[pair]:
            new_counts[pair] += count

    return new_counts


with open('input.txt') as f:
    starting_polymer = f.readline().strip()
    last_letter = starting_polymer[-1]
    polymer_pair_counts = pair_counts(starting_polymer)

    next(f)
    pair_transform_rules = defaultdict(list)
    for line in f:
        pair, new_letter = line.strip().split(' -> ')
        pair_transform_rules[pair] = (pair[0] + new_letter, new_letter + pair[1])

for i in range(40):
    polymer_pair_counts = update_pair_counts(polymer_pair_counts, pair_transform_rules)

letter_counts = defaultdict(int)

letter_counts[last_letter] += 1

for pair, count in polymer_pair_counts.items():
    letter_counts[pair[0]] += count

char_counts = letter_counts.values()

print(max(char_counts) - min(char_counts))
