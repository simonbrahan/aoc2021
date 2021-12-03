from collections import defaultdict

with open('input.txt') as f:
    report = [line.strip() for line in f]

on_bit_counts = defaultdict(int)
bitset_count = 0
for bitset in report:
    bitset_count += 1
    for idx, bit in enumerate(bitset):
        if bit == '1':
            on_bit_counts[idx] += 1

majority_bit_count = bitset_count / 2

gamma_bit_list = ''
epsilon_bit_list = ''
for i in range(0, len(on_bit_counts)):
    if on_bit_counts[i] > majority_bit_count:
        gamma_bit_list += '1'
        epsilon_bit_list += '0'
    else:
        gamma_bit_list += '0'
        epsilon_bit_list += '1'

print(int(gamma_bit_list, 2) * int(epsilon_bit_list, 2))
