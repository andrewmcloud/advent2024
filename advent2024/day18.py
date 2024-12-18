import heapq
import re
from collections import defaultdict

with open("../input/day18.txt", "r") as f:
    input_ = f.readlines()

coords = []
for line in input_:
    r, c = [int(x) for x in re.findall(r"-?\d+", line)]
    coords.append((r, c))

maze = [["."] * 71 for _ in range(71)]
for c, r in coords[:2934]:
    maze[r][c] = "#"


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


def build_maze(limit: int) -> list[list[str]]:
    maze = [["."] * 71 for _ in range(71)]
    for c, r in coords[:limit]:
        maze[r][c] = "#"
    return maze


def search(coords: list[tuple[int, int]]) -> str:
    start, end = 1024, len(coords)
    while True:
        if start + 1 == end:
            return ",".join([str(x) for x in coords[start]])
        mid = start + (end - start) // 2
        score, _ = dijkstra(build_maze(mid), (0, 0), (70, 70))
        if score == -1:
            end = mid
        else:
            start = mid


part1, _ = dijkstra(build_maze(1024), (0, 0), (70, 70))
part2 = search(coords)

print(f"part 1: {part1}")
print(f"part 2: {part2}")
