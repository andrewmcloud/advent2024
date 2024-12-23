from collections import defaultdict

with open("../input/day22.txt", "r") as f:
    input_ = [int(x) for x in f.readlines()]


def next_secret(secret: int) -> int:
    s1 = (int(secret * 64) ^ secret) % 16777216
    s2 = (int(s1 / 32) ^ s1) % 16777216
    s3 = ((s2 * 2048) ^ s2) % 16777216
    return s3


bananas = defaultdict(int)
total_secrets = 0

for secret in input_:
    seen = set()
    secrets = [input_[0]] + [secret := next_secret(secret) for _ in range(2000)]
    total_secrets += secrets[-1]
    price_changes = [secrets[i+1] % 10 - secrets[i] % 10 for i in range(len(secrets) - 1)]

    for i in range(len(secrets) - 4):
        consecutive_changes = tuple(price_changes[i:i+4])
        if consecutive_changes in seen:
            continue
        # we are looking for the price @ the first sequence appearance
        seen.add(consecutive_changes)
        bananas[consecutive_changes] += secrets[i+4] % 10

print(f"part 1: {total_secrets}")
print(f"part 2: {max(bananas.values())}")
