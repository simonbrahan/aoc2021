from dijkstra import get_risk

with open('input.txt') as f:
    grid = [[int(risk) for risk in line.strip()] for line in f]

print(get_risk(grid))
