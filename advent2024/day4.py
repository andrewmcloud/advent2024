import re

with open("../input/day4.txt", "r") as f:
    ws = [line.strip() for line in f.readlines()]


def diagonals(x: list) -> list:
    diags = []
    for d in range(-(len(x) - 1), len(x)):
        diag = [x[i][i-d] for i in range(max(0, d), min(len(x), len(x) + d))]
        if diag:
            diags.append(diag)
    return [''.join(d) for d in diags]


def windows(x: list) -> list:
    windows = []
    for i in range(len(x[0]) - 2):
        for j in range(len(x) - 2):
            windows.append([x[j][i:i+3], x[j+1][i:i+3], x[j+2][i:i+3]])
    return windows


def horizontals(x: list) -> list:
    return [line for line in x]


def verticals(x: list) -> list:
    return [''.join([y[i] for y in x]) for i in range(len(x[0]))]


# part 1
all_ways = horizontals(ws) + verticals(ws) + diagonals(ws) + diagonals(ws[::-1])
part1 = sum(len(re.findall(r"(?=XMAS)|(?=SAMX)", line)) for line in all_ways)

# part 2
count = 0
for window in windows(ws):
    mas = 0
    for diag in diagonals(window) + diagonals(window[::-1]):
        m = re.findall(r"MAS|SAM", diag)
        mas += 1 if m else 0
    count += 1 if mas > 1 else 0

print(f"part 1: {part1}")
print(f"part 2: {count}")
