import heapq
from collections import defaultdict

with open("../input/day16.txt") as f:
    lines = f.readlines()

maze = [line.strip() for line in lines]

DIRS = {"N": (-1, 0), "E": (0, 1), "S": (1, 0), "W": (0, -1)}
NS = {"N", "S"}
EW = {"E", "W"}


def find_start(maze: list[str]) -> tuple[int, int]:
    for r, row in enumerate(maze):
        for c, col in enumerate(row):
            if col == "S":
                return r, c
    return -1, -1


def dijkstra(maze: list[str], start: tuple[int, int]) -> tuple[int, list[tuple[int, int]]]:
    pq = [(0, start, "E", [start])]
    distances = defaultdict(lambda: float("inf"))
    distances[start] = 0
    while pq:
        score, (r, c), traveling, path = heapq.heappop(pq)

        if maze[r][c] == "E":
            return score, path

        for d in "NSEW":
            nr, nc = r + DIRS[d][0], c + DIRS[d][1]
            turn = (traveling in NS and d in EW) or (traveling in EW and d in NS)
            points = 1001 if turn else 1
            if maze[nr][nc] != "#" and (nr, nc) and points < distances[(nr, nc)]:
                distances[(nr, nc)] = points
                heapq.heappush(pq, (score + points, (nr, nc), d, path[:] + [(nr, nc)]))

    return -1, []


start = find_start(maze)
score, path = dijkstra(maze, start)

print(f"part 1: {score}")


# part 2 attempt
# seats = set()
# for (r, c) in path:
#     if maze[r][c] == "S" or maze[r][c] == "E":
#         continue
#     maze[r] = maze[r][:c] + "#" + maze[r][c+1:]
#     cost, p = dijkstra(maze, start)
#     if cost == score:
#         seats.update(set(p))
#     maze[r] = maze[r][:c] + "." + maze[r][c+1:]
#
# print(len(seats)+2)
