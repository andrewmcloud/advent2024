from dataclasses import dataclass

with open("../input/day12.txt") as f:
    input_ = [line.strip() for line in f.readlines()]


@dataclass
class Directions:
    n: bool
    ne: bool
    e: bool
    se: bool
    s: bool
    sw: bool
    w: bool
    nw: bool


def count_corners(points):
    corners = 0
    for point in points:
        r, c = point
        d = Directions
        d.n = (r-1, c) in points
        d.ne = (r-1, c+1) in points
        d.e = (r, c+1) in points
        d.se = (r+1, c+1) in points
        d.s = (r+1, c) in points
        d.sw = (r+1, c-1) in points
        d.w = (r, c-1) in points
        d.nw = (r-1, c-1) in points

        corners += 1 if not d.n and not d.e else 0
        corners += 1 if not d.e and not d.s else 0
        corners += 1 if not d.s and not d.w else 0
        corners += 1 if not d.w and not d.n else 0
        corners += 1 if (d.n and d.e) and not d.ne else 0
        corners += 1 if (d.e and d.s) and not d.se else 0
        corners += 1 if (d.s and d.w) and not d.sw else 0
        corners += 1 if (d.w and d.n) and not d.nw else 0

    return corners


def is_valid(entry, plant, visited, map) -> bool:
    r, c = entry
    return (0 <= r < len(map)
            and 0 <= c < len(map[0])
            and entry not in visited
            and map[r][c] == plant
            )


def fence(points):
    length = 0
    for point in points:
        r, c = point
        for rr, cc in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            nr, nc = (r + rr, c + cc)
            if (nr, nc) not in points:
                length += 1
    return length


def find_garden(map):
    gardens = []
    visited = set()

    def dfs(entry, plant, garden):
        if not is_valid(entry, plant, visited, map):
            return

        garden.append(entry)
        visited.add(entry)
        r, c = entry
        for rr, cc in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            dfs((r+rr, c+cc), plant, garden)
        return garden

    for r, row in enumerate(map):
        for c, col in enumerate(row):
            if (r, c) in visited:
                continue
            garden = dfs((r, c), map[r][c], [])
            gardens.append(garden)
    return gardens


plots = find_garden(input_)
part1 = sum(len(plot) * fence(plot) for plot in plots)
part2 = sum(len(plot) * count_corners(plot) for plot in plots)

print(f"part 1: {part1}")
print(f"part 2: {part2}")
