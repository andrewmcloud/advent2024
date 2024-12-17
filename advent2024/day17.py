import re
with open("../input/day17.txt", "r") as f:
    input_ = f.read()

registers, program = input_.split("\n\n")
registers = registers.split("\n")

[A] = [int(x) for x in re.findall(r"\d+", registers[0])]
[B] = [int(x) for x in re.findall(r"-?\d+", registers[1])]
[C] = [int(x) for x in re.findall(r"-?\d+", registers[2])]

program = [int(x) for x in re.findall(r"-?\d+", program)]


def combo():
    return {0: 0, 1: 1, 2: 2, 3: 3, 4: A, 5: B, 6: C}


output = []
pointer = 0

while True:
    if pointer >= len(program)-1:
        print(",".join([str(x) for x in output]))
        break

    instruction = program[pointer]
    operand = program[pointer+1]
    pointer += 2

    match instruction:
        case 0:
            A = int(A / 2**combo()[operand])
        case 1:
            B = B ^ operand
        case 2:
            B = combo()[operand] % 8
        case 3:
            if A == 0:
                continue
            else:
                pointer = operand
        case 4:
            B = B ^ C
        case 5:
            output.append(combo()[operand] % 8)
        case 6:
            B = int(A / 2 ** combo()[operand])
        case 7:
            C = int(A / 2 ** combo()[operand])