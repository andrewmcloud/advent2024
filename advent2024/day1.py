from collections import Counter

left, right = [], []
with open("../input/day1.txt", "r") as f:
    for line in f.readlines():
        l, r = line.split()
        left.append(int(l))
        right.append(int(r))

# part 1
t = zip(sorted(left), sorted(right))
part1 = sum(abs(l - r) for (l, r) in t)

# part 2
r_counter = Counter(right)
part2 = sum(x * r_counter[x] for x in left)
print(part2)
