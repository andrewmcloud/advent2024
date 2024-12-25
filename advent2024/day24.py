with open("../input/day24.txt", "r") as f:
    init, instructions = f.read().split("\n\n")
    init = init.split("\n")
    instructions = instructions.split("\n")

OP = {
    "OR": lambda a, b: a | b,
    "AND": lambda a, b: a & b,
    "XOR": lambda a, b: a ^ b
}

wires = {wire: int(bit) for wire, bit in (x.split(": ") for x in init)}
initialization = set(wires.keys())

z_wires = set()
operations = []
for instruction in instructions:
    left, w3 = instruction.split(" -> ")
    w1, op, w2 = left.split(" ")
    if w3.startswith("z"):
        z_wires.add(w3)
    operations.append((w1, op, w2, w3))

seen = set()
while True:
    for i, operation in enumerate(operations):
        w1, op, w2, w3 = operation
        if (wire1 := wires.get(w1)) is not None and (wire2 := wires.get(w2)) is not None:
            wires[w3] = OP[op](wire1, wire2)
            operations.pop(i)
            seen.add(w3)
    if z_wires <= seen:
        break

y = sorted([(k, v) for k, v in wires.items() if k.startswith("z")], key=lambda a: a[0])
part1 = int("".join([str(a[1]) for a in y])[::-1], 2)

print(f"part 1: {part1}")
