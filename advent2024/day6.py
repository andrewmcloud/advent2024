from itertools import cycle

with open("../input/day6.txt", "r") as f:
    grid = [list(line) for line in f.read().strip().split("\n")]

directions = cycle([(-1, 0), (0, 1), (1, 0), (0, -1)])


def find_start(grid):
    for y, line in enumerate(grid):
        for x, ch in enumerate(line):
            if ch == "^":
                return y, x
    raise Exception("no start")


def move(grid, directions):
    visited = set()
    current_position = find_start(grid)
    visited.add(current_position)
    direction = next(directions)

    while True:
        next_position = (current_position[0] + direction[0], current_position[1] + direction[1])
        if next_position[0] < 0 or next_position[0] > len(grid[0]) - 1 or next_position[1] < 0 or next_position[1] > len(grid) - 1:
            return visited

        element = grid[next_position[0]][next_position[1]]
        if element == "#":
            direction = next(directions)
        else:
            visited.add(next_position)
            current_position = next_position


# part 1:
part1 = len(move(grid, directions))

print(f"part1: {part1}")

