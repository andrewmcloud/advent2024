from typing import Optional

with open("../input/day7.txt", "r") as f:
    lines = f.readlines()

equations = []
for line in lines:
    r, ns = line.strip().split(": ")
    equations.append((int(r), [int(n) for n in ns.split(" ")]))


def add(x, y):
    return x + y


def multiply(x, y):
    return x * y


def concat(x, y):
    return int(str(x) + str(y))


functions = {
    "+": add,
    "*": multiply,
    "|": concat
}


def calibrate(result: int, numbers: list[int], operators: list[str]) -> int:
    def evaluate(total: int, remaining: list[int]) -> Optional[int]:
        if not remaining:
            return result if total == result else None

        for operator in operators:
            next_, rest = remaining[0], remaining[1:]
            if test_value := evaluate(functions[operator](total, next_), rest):
                return test_value
        return 0

    return evaluate(numbers[0], numbers[1:])


part1 = sum(calibrate(t, nums, ["+", "*"]) for (t, nums) in equations)
part2 = sum(calibrate(t, nums, ["+", "*", "|"]) for (t, nums) in equations)

print(f"part 1: {part1}")
print(f"part 2: {part2}")
