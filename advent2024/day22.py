with open("../input/day22.txt", "r") as f:
    secrets = [int(x) for x in f.readlines()]


def next_secret(secret: int) -> int:
    s1 = (int(secret * 64) ^ secret) % 16777216
    s2 = (int(s1 / 32) ^ s1) % 16777216
    s3 = ((s2 * 2048) ^ s2) % 16777216
    return s3


results = []
for secret in secrets:
    for _ in range(2000):
        secret = next_secret(secret)
    results.append(secret)
part1 = sum(results)

print(f"part 1: {part1}")
