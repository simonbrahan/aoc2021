from diagreport import gamma_epsilon

with open('input.txt') as f:
    report = [line.strip() for line in f]

gamma, epsilon = gamma_epsilon(report)

print(int(gamma, 2) * int(epsilon, 2))
