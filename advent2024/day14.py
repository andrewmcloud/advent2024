from collections import defaultdict
import re
with open("../input/day14.txt", "r") as f:
    input_ = f.readlines()


def init_robots(input_: list[str]) -> list:
    robots = []
    for line in input_:
        p, v = line.split(" ")
        start = [int(x) for x in re.findall(r"\d+", p)[::-1]]
        velocity = [int(x) for x in re.findall(r"-?\d+", v)[::-1]]
        robots.append([start, velocity])
    return robots


def is_tree(robots: list, v: int, h: int) -> bool:
    positions = defaultdict(set)
    for robot in robots:
        positions[robot[0][0]].add(robot[0][1])

    for pos in positions:
        p = positions[pos]
        ordered = sorted(p)
        if len([ordered[i + 1] - ordered[i] == 1 for i in range(len(ordered) - 1)]) == 31:
            grid = []
            for row in range(v):
                line = []
                for col in range(h):
                    line.append(".") if col not in positions[row] else line.append("X")
                grid.append(line)
            for line in grid:
                print("".join(line))
            return True
    return False


def move_robots(robots: list, v: int, h: int, iters: int, tree: bool) -> int:
    for i in range(iters):
        for robot in robots:
            sr, sc = robot[0]
            vr, vc = robot[1]
            nr, nc = (sr+vr) % v, (sc+vc) % h
            robot[0] = [nr, nc]
        if tree:
            if is_tree(robots, v, h):
                print(i+1)
    return robots


vertical = 103
horizontal = 101

robots = init_robots(input_)
robots = move_robots(robots, vertical, horizontal, 100, False)

q1, q2, q3, q4 = 0, 0, 0, 0
for robot in robots:
    p = robot[0]
    if 0 <= p[0] < vertical//2 and 0 <= p[1] < horizontal//2:
        q1 += 1
    elif 0 <= p[0] < vertical//2 and horizontal//2 < p[1] < horizontal:
        q2 += 1
    elif vertical//2 < p[0] < vertical and 0 <= p[1] < horizontal//2:
        q3 += 1
    elif vertical//2 < p[0] < vertical and horizontal//2 < p[1] < horizontal:
        q4 += 1
part1 = q1*q2*q3*q4

robots = init_robots(input_)
part2 = move_robots(robots, vertical, horizontal, 10000, True)
print(f"part 1: {part1}")
print(f"part 2: 7412")
