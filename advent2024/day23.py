from collections import defaultdict
from itertools import combinations
from typing import Optional

with open("../input/day23.txt", "r") as f:
    input_ = [x.strip() for x in f.readlines()]

network = defaultdict(set)
connections = set()

for line in input_:
    c1, c2 = line.split("-")
    network[c1].add(c2)
    network[c2].add(c1)

computers = network.keys()
threes = list(combinations(computers, 3))
networked = set()

for three in threes:
    x, y, z = three
    if x[0] == "t" or y[0] == "t" or z[0] == "t":
        if y in network[x] and z in network[x] and y in network[z]:
            networked.add(three)


# https://en.wikipedia.org/wiki/Bron%E2%80%93Kerbosch_algorithm
def bron_kerbosch(
    g: dict[str, set[str]],
    r: Optional[set] = None,
    p: Optional[set] = None,
    x: Optional[set] = None
):
    if r is None:
        r = set()
    if p is None:
        p = set(g.keys())
    if x is None:
        x = set()

    cliques = []
    if not p and not x:
        cliques.append(r)
        return cliques

    for v in list(p):
        neighbors = set(g[v])
        cliques.extend(bron_kerbosch(g, r | {v}, p & neighbors, x & neighbors))
        p.remove(v)
        x.add(v)

    return cliques


# print(max(len(clique) for clique in bron_kerbosch(network)))
x = list([clique for clique in bron_kerbosch(network) if len(clique) == 13][0])
x.sort()

part1 = len(networked)
part2 = (",".join(x))

print(f"part 1: {part1}")
print(f"part 2: {part2}")
