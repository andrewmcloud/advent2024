from collections import Counter
with open("../input/day11.txt", "r") as f:
    input_ = f.read().split()


def split_stone(stone: str) -> tuple[str, str]:
    return stone[:len(stone)//2], str(int(stone[len(stone)//2:]))


def blink(s: tuple[str, int], stones: dict[str, int]) -> None:
    for (n, c) in s:
        match n:
            case "0":
                stones["1"] += 1 * c
            case _ if len(n) % 2 == 0:
                s1, s2 = split_stone(n)
                stones[s1] += 1 * c
                stones[s2] += 1 * c
            case _:
                stones[str(int(n)*2024)] += 1 * c
        stones[n] -= 1 * c


def blinking(blinks: int) -> dict[str, int]:
    stones = Counter()
    for stone in input_:
        stones[stone] += 1

    for _ in range(blinks):
        s = [(k, v) for k, v in stones.items() if v > 0]
        blink(s, stones)
    return stones


part1 = sum(c for _, c in blinking(25).items())
part2 = sum(c for _, c in blinking(75).items())

print(f"part 1: {part1}")
print(f"part 2: {part2}")
