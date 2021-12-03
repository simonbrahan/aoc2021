from diagreport import gamma_epsilon

with open('sample.txt') as f:
    report = [line.strip() for line in f]

gamma, epsilon = gamma_epsilon(report)

oxygen_ratings = report.copy()

check_bit = 0
i = 0
while len(oxygen_ratings) > 1:
    if gamma[check_bit] == 't':
        check_val = 1
    else:
        check_val = gamma[check_bit]

    if oxygen_ratings[i][check_bit] != check_val:
        oxygen_ratings.pop(i)
    else:
        i += 1

    if i >= len(oxygen_ratings):
        gamma, _ = gamma_epsilon(oxygen_ratings)
        check_bit += 1
        i = 0

oxygen_rating = oxygen_ratings[0]

scrubber_ratings = report.copy()

check_bit = 0
i = 0
while len(scrubber_ratings) > 1:
    if epsilon[check_bit] == 't':
        check_val = 0
    else:
        check_val = epsilon[check_bit]

    if scrubber_ratings[i][check_bit] != check_val:
        scrubber_ratings.pop(i)
    else:
        i += 1

    if i >= len(scrubber_ratings):
        _, epsilon = gamma_epsilon(scrubber_ratings)
        check_bit += 1
        i = 0

scrubber_rating = scrubber_ratings[0]

print(int(oxygen_rating, 2) * int(scrubber_rating, 2))
