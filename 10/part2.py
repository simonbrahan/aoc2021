from chunks import get_first_error, get_missing_chars

with open('input.txt') as f:
    lines = [line.strip() for line in f]

char_scores = {')': 1, ']': 2, '}': 3, '>': 4}
line_scores = []
for line in lines:
    first_error = get_first_error(line)

    if first_error:
        continue

    missing_chars = get_missing_chars(line)

    line_score = 0
    for char in missing_chars:
        line_score *= 5
        line_score += char_scores[char]

    line_scores.append(line_score)

line_scores.sort()
print(line_scores[int(len(line_scores) / 2)])
