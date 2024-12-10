from typing import Optional

with open("../input/day9.txt", "r") as f:
    input_ = f.read()


def build_disk1(in_: str) -> list[int]:
    fs = [x for i, x in enumerate(in_) if i % 2 == 0]
    files = []
    for i, file in enumerate(fs):
        files += [i] * int(file)
    return files[::-1]


def solve_part1(disk: list[int]):
    num_files = len(disk)
    compressed = []
    for i, x in enumerate(input_):
        if i % 2 == 0:  # this is a file
            new = [i//2] * int(x)
            if len(compressed) + len(new) > num_files:
                remains = len(compressed) + len(new) - num_files
                compressed += new[:len(new)-remains]
                return compressed
            compressed += [i//2] * int(x)
        if i % 2 == 1:  # this is free space
            if len(compressed) + int(x) > num_files:
                remains = len(compressed) + int(x) - num_files
                compressed += disk[:int(x)-remains]
                return compressed
            compressed += disk[:int(x)]
            disk = disk[int(x):]
    return compressed


def build_disk2(in_: str) -> list[list[int]]:
    fs = [x for i, x in enumerate(in_) if i % 2 == 0]
    files = []
    for i, file in enumerate(fs):
        files.append([i] * int(file))
    return files[::-1]


def build_file_system(in_):
    fs = []
    for i, x in enumerate(in_):
        if i % 2 == 0:  # this is a file
            fs += [i // 2] * int(x)
        if i % 2 != 0:  # this is free
            fs += [None] * int(x)
    return fs


# naive solution, because AOC beat me today. I couldn't figure out what
# was wrong with my fast solution.
def solve_part2(fs: list[Optional[int]], disk: list[list[int]]):
    for d in disk[:-1]:
        for i, f in enumerate(fs):
            # only check free space before the file location
            if f == d[0]:
                break
            if f is None:
                # look ahead to see how much room we have
                free = 0
                for j, next_ in enumerate(fs[i:]):
                    if next_:
                        free = j
                        break

                if len(d) <= free:
                    new = [0 if x == d[0] else x for x in fs[i + len(d):]]
                    fs = fs[:i]+d+new
                    break
    return fs


part1 = sum(i*int(fb) for i, fb in enumerate(solve_part1(build_disk1(input_))))

fs = build_file_system(input_)
disk = build_disk2(input_)

cleaned = [0 if x is None else x for x in solve_part2(fs, disk)]

part2 = sum(i*fb for i, fb in enumerate(cleaned))

print(f"part1: {part1}")
print(f"part1: {part2}")
