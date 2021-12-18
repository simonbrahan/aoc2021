from chunks import get_first_error

with open('input.txt') as f:
    lines = [line.strip() for line in f]

error_scores = {')': 3, ']': 57, '}': 1197, '>': 25137}

error_total = 0
for line in lines:
    first_error = get_first_error(line)

    if first_error:
        error_total += error_scores[first_error]

print(error_total)
