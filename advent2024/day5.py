from collections import defaultdict
with open("../input/day5.txt", "r") as f:
    input_ = f.read()

rules, pages = input_.strip().split("\n\n")
rules = rules.strip().split("\n")

pages = pages.strip().split("\n")
pages = [[int(x) for x in page.split(",")] for page in pages]

lookup = defaultdict(set)
for rule in rules:
    (k, v) = rule.split("|")
    lookup[int(k)].add(int(v))


def is_ordered(entry: list[int], lookup: dict[int, set[int]]):
    for i, e in enumerate(entry):
        for x in entry[i:]:
            if e in lookup[x]:
                return False
    return True


def find_first(entry: list[int], lookup: dict[int, set[int]]):
    for i, e1 in enumerate(entry):
        not_found = []
        for j, e2 in enumerate(entry):
            if i == j:
                continue
            if e1 in lookup[e2]:
                not_found.append(False)
            not_found.append(True)
        if all(not_found):
            return i
    raise Exception("oh shit!")


def order(entry: list[int], lookup: dict[int, set[int]]):
    ordered = []
    while entry:
        first = find_first(entry, lookup)
        ordered.append(entry[first])
        entry.pop(first)
    return ordered

# part 1
ordered = [page for page in pages if is_ordered(page, lookup)]
part1 = sum(o[len(o) // 2] for o in ordered)

# part 2
unordered = [page for page in pages if not is_ordered(page, lookup)]
ordered = [order(no, lookup) for no in unordered]
part2 = sum(o[len(o) // 2] for o in ordered)

print(f"part1: {part1}")
print(f"part2: {part2}")
