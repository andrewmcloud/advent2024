with open("../input/day2.txt") as f:
    reports = [[int(y) for y in line.split()] for line in f.readlines()]


def safe(report: list[int]) -> bool:
    if report[0] > report[1]:
        return all(1 <= (x - y) <= 3 for x, y in zip(report, report[1:]))
    if report[0] < report[1]:
        return all(1 <= (y - x) <= 3 for x, y in zip(report, report[1:]))
    return False


def safe2(report: list[int]) -> bool:
    return any(
        [safe(report)] +
        [safe(report[:i] + report[i + 1:]) for i in range(len(report))]
    )


part1 = sum(safe(report) for report in reports)
part2 = sum(safe2(report) for report in reports)

print(f"part 1: {part1}")
print(f"part 2: {part2}")
