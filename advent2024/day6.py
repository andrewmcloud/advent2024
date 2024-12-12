from itertools import cycle

with open("../input/day6.txt", "r") as f:
    grid = [list(line) for line in f.read().strip().split("\n")]


def find_start(grid):
    for y, line in enumerate(grid):
        for x, ch in enumerate(line):
            if ch == "^":
                return y, x
    raise Exception("no start")


def move(grid:list) -> tuple[set, bool]:
    directions = cycle([(-1, 0), (0, 1), (1, 0), (0, -1)])
    visited = set()
    current_position = find_start(grid)
    direction = next(directions)
    visited.add((current_position, direction))

    while True:
        next_position = (current_position[0] + direction[0], current_position[1] + direction[1])
        if next_position[0] < 0 or next_position[0] > len(grid[0]) - 1 or next_position[1] < 0 or next_position[1] > len(grid) - 1:
            return visited, False

        element = grid[next_position[0]][next_position[1]]

        if element == "#":
            direction = next(directions)
        else:
            if (next_position, direction) in visited:
                return set(), True
            visited.add((next_position, direction))
            current_position = next_position


# part 1:
part1 = {m[0] for m in move(grid)[0]}

# part 2
count = []
for (i, j) in part1:
    if grid[i][j] == "#" or grid[i][j] == "^":
        continue
    grid[i][j] = "#"
    count.append(move(grid)[1])
    grid[i][j] = "."
part2 = sum(count)

print(f"part 1: {len(part1)}")
print(f"part 2: {part2}")
