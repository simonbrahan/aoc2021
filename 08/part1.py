with open('input.txt') as f:
    filtered_digit_count = 0
    for line in f:
        for digit in line.split(' | ')[1].strip().split(' '):
            if len(digit) in [2, 4, 3, 7]:
                filtered_digit_count += 1

print(filtered_digit_count)

