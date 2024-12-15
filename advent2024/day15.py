with open("../input/day15.txt", "r") as f:
    warehouse, instructions = f.read().split("\n\n")

warehouse = warehouse.splitlines()
instructions = "".join(instructions.splitlines())

move = {"^": (-1, 0), ">": (0, 1), "v": (1, 0), "<": (0, -1)}


def find_robot(warehouse: list[list[str]]):
    for r, row in enumerate(warehouse):
        for c, col in enumerate(row):
            if col == "@":
                return r, c


def print_warehouse(warehouse: list[list[str]]):
    for row in warehouse:
        print(row)
    print("\n")


def move_to_front(s: str, c: str):
    wall = s.index("#")
    index = s[:wall].find(c)
    if index == -1:
        return s
    return c + s[:index] + s[index + 1:]


def push_boxe(next_: tuple[int, int], instruction: str, warehouse: list[list[str]]):
    if instruction == "^":
        row = "".join([warehouse[i][next_[1]] for i in range(0, len(warehouse))])
        up = row[:next_[0]+1]
        down = row[next_[0]+1:]
        # flip `up` over before and after move_to_front since the robot is traveling north (backwards)
        push = move_to_front(up[::-1], ".")
        new = push[::-1] + down, push[0] == "."
    if instruction == "v":
        row = "".join([warehouse[i][next_[1]] for i in range(0, len(warehouse))])
        up = row[:next_[0]]
        down = row[next_[0]:]
        push = move_to_front(down, ".")
        new = up + push, push[0] == "."
    if instruction == ">":
        right = warehouse[next_[0]][next_[1]:]
        push = move_to_front(right, ".")
        new = warehouse[next_[0]][:next_[1]] + push, push[0] == "."
    if instruction == "<":
        left = warehouse[next_[0]][:next_[1]+1]
        # flip `left` over before and after move_to_front since the robot is traveling west (backwards)
        push = move_to_front(left[::-1], ".")
        new = push[::-1] + warehouse[next_[0]][next_[1]+1:], push[0] == "."
    return new


def push_boxes(warehouse: list[list[str]], robot: tuple[int, int], instructions: str):
    for instruction in instructions:
        d = move[instruction]
        next_ = warehouse[robot[0] + d[0]][robot[1] + d[1]]
        match next_:
            case ".": robot = robot[0]+d[0], robot[1]+d[1]
            case "#": robot = robot
            case "O":
                pos = robot[0] + d[0], robot[1] + d[1]
                moved, move_robot = push_boxe(pos, instruction, warehouse)
                if instruction in {"<", ">"}:
                    warehouse[robot[0]] = moved
                else:
                    for i, c in enumerate(moved):
                        warehouse[i] = warehouse[i][:pos[1]]+c+warehouse[i][pos[1]+1:]
                robot = (robot[0] + d[0], robot[1] + d[1]) if move_robot else robot
    # print_warehouse(warehouse)


robot = find_robot(warehouse)
warehouse[robot[0]] = warehouse[robot[0]].replace("@", ".")
push_boxes(warehouse, robot, instructions)

total = 0
for r, row in enumerate(warehouse):
    for c, col in enumerate(row):
        if warehouse[r][c] == "O":
            total += 100 * r + c

print(f"part 1: {total}")
