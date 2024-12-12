from collections import defaultdict

with open("../input/day8.txt", "r") as f:
    grid = [x.strip() for x in f.readlines()]


antennas = defaultdict(set)
for x, line in enumerate(grid):
    for y, elem in enumerate(line):
        a = grid[x][y]
        if a != ".":
            antennas[a].add((x, y))


def in_bounds(coord: tuple[int, int]) -> bool:
    return True if (0 <= coord[0] < len(grid)) and (0 <= coord[1] < len(grid[0])) else False


def find_all(curr: tuple[int, int], offset: tuple[int, int]) ->set[tuple[int, int]]:
    coords = set()
    coords.add(curr)
    antinode = (curr[0] + offset[0], curr[1] + offset[1])

    while in_bounds(antinode):
        coords.add(antinode)
        antinode = antinode[0] + offset[0], antinode[1] + offset[1]
    return coords


def antinodes(antennas: set[tuple[int, int]], harmonics: bool = False):
    coords = set()
    for a1 in antennas:
        for a2 in antennas:
            if a1 == a2:
                continue
            d = (a1[0] - a2[0], a1[1] - a2[1])
            if harmonics:
                curr = a1
                coords = coords | find_all(curr, d)
            else:
                antinode = (a1[0] + d[0], a1[1] + d[1])
                if in_bounds(antinode):
                    coords.add(antinode)
    return coords


part1 = len({antinode for k in antennas.keys() for antinode in antinodes(antennas[k], False)})
part2 = len({antinode for k in antennas.keys() for antinode in antinodes(antennas[k], True)})

print(f"part 1: {part1}")
print(f"part 2: {part2}")
