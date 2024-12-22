import heapq
from collections import defaultdict


with open("../input/day20_test.txt") as f:
    lines = f.readlines()

maze = [[x for x in line.strip()] for line in lines]


def find_start_end(maze: list[list[str]]) -> list[tuple[int, int]]:
    coords = []
    for r, row in enumerate(maze):
        for c, col in enumerate(row):
            if col == "S":
                coords.append((r, c))
            if col == "E":
                coords.append((r, c))
    if not coords:
        raise Exception
    return coords


def dijkstra(maze: list[list[str]], start: tuple[int, int], end: tuple[int, int]) -> tuple[int, list[tuple[int, int]]]:
    pq = [(0, start, [start])]
    distances = defaultdict(lambda: float("inf"))
    distances[start] = 0
    while pq:
        score, (r, c), path = heapq.heappop(pq)

        if (r, c) == end:
            return score, path

        for rr, cc in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            nr, nc = r + rr, c + cc
            points = 1
            if (
                    0 <= r < len(maze)
                    and 0 <= c < len(maze[0])
                    and maze[r][c] != "#"
                    and points < distances[(nr, nc)]
            ):
                distances[(nr, nc)] = points
                heapq.heappush(pq, (score + points, (nr, nc), path[:] + [(nr, nc)]))

    return -1, []


def find_adjacent(maze: list[list[str]], path: list[tuple[int, int]]):
    adjacent = set()
    for node in path:
        r, c = node
        for rr, cc in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            nr, nc = r + rr, c + cc
            nnr, nnc = nr + rr, nc + cc
            if (
                    maze[nr][nc] == "#"
                    and 0 < r < len(maze) - 1
                    and 0 < c < len(maze[0]) - 1
                    and 0 < nnr < len(maze)
                    and 0 < nnc < len(maze[0])
                    and maze[nnr][nnc] == "."
                    and (nnr, nnc) != (r, c)
            ):
                adjacent.add((nr, nc))
    return adjacent


start, end = find_start_end(maze)
race_score, race_path = dijkstra(maze, start, end)
adjacent_nodes = find_adjacent(maze, race_path)


cheats = []
for node in adjacent_nodes:
    r, c = node
    maze[r][c] = "."
    cheat, _ = dijkstra(maze, start, end)
    maze[r][c] = "#"
    if cheat < race_score:
        cheats.append(race_score - cheat)

part1 = sum(1 for x in cheats if x >= 100)
print(f"part 1: {part1}")
