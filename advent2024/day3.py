import re

with open("../input/day3.txt", "r") as f:
    x = f.read()


def total(matches: list[tuple[str]]) -> int:
    do = True
    t = 0
    pairs = [tuple(filter(None, item)) for item in matches]
    for pair in pairs:
        match pair[0]:
            case "don't": do = False
            case "do": do = True
            case _: t += int(pair[0]) * int(pair[1]) if do else 0
    return t


# part 1
instructions = re.findall(r'mul\((\d{1,3}),(\d{1,3})\)', x)
part1 = sum(int(instruction[0]) * int(instruction[1]) for instruction in instructions)

# part 2
instructions = re.findall(r'mul\((\d{1,3}),(\d{1,3})\)|(don\'t)\(\)|(do)\(\)', x)
part2 = total(instructions)

print(f"part 1: {part1}")
print(f"part 2: {part2}")
