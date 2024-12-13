import re
with open ("../input/day13.txt", "r") as f:
    input_ = f.read()

games = input_.split("\n\n")


def claw_game(make_it_high: bool):
    tokens = 0
    for game in games:
        button_a, button_b, prize = game.split("\n")

        x1, x2 = [int(x) for x in re.findall(r"\d+", button_a)]
        y1, y2 = [int(x) for x in re.findall(r"\d+", button_b)]
        z1, z2 = [int(x) for x in re.findall(r"\d+", prize)]

        z1 += 10000000000000 if make_it_high else 0
        z2 += 10000000000000 if make_it_high else 0

        b = int((z2 * x1 - x2 * z1) / (y2 * x1 - x2 * y1))
        a = int((z1 - b * y1) / x1)

        if x1 * a + y1 * b == z1 and x2 * a + y2 * b == z2:
            tokens += 3 * a + b
    return tokens


print(f"part 1: {claw_game(False)}")
print(f"part 2: {claw_game(True)}")
