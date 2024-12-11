with open("../input/day10.txt", "r") as f:
    input_ = f.readlines()


def find_trail_heads(map: list[list[int]]):
    return [(y, x) for y, row in enumerate(map) for x, step in enumerate(row) if step == 0]


def is_valid(row, col, curr):
    return 0 <= row < len(map) and 0 <= col < len(map[0]) and map[row][col] == curr + 1


def find_all(map, row, col):
    paths = []
    visited = set()

    def backtrack(r, c, path):
        if map[r][c] == 9:
            paths.append(path[:])
            return

        visited.add((r, c))
        curr = map[r][c]
        for rr, cc in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            r1, c1 = r + rr, c + cc
            if is_valid(r1, c1, curr):
                path.append((r1, c1))
                backtrack(r1, c1, path)
                path.pop()
        visited.remove((r, c))

    backtrack(row, col, [(row, col)])
    return paths


map = [[int(x) for x in line.strip()] for line in input_]
trail_heads = find_trail_heads(map)
trails = [find_all(map, row, col) for ((row, col)) in trail_heads]

part1 = sum(len({route[-1] for route in trail}) for trail in trails)
part2 = sum(len(trail) for trail in trails)

print(f"part1: {part1}")
print(f"part1: {part2}")
