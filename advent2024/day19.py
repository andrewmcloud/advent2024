with open("../input/day19.txt", "r") as f:
    input_ = f.read()

towels, patterns = input_.split("\n\n")
towels = towels.strip().split(", ")
patterns = patterns.split("\n")


def part1():
    def search(pattern, partial=""):
        if partial == pattern:
            return True

        for towel in towels:
            if pattern.startswith(partial + towel):
                if search(pattern, partial + towel):
                    return True
        return False

    return sum(search(pattern) for pattern in patterns)


def part2(patterns, towels):
    options = []

    for pattern in patterns:
        n = len(pattern)
        dp = [0] * (n + 1)
        dp[0] = 1

        for i in range(1, n + 1):
            for towel in towels:
                m = len(towel)
                dp[i] += dp[i-m] if i >= len(towel) and pattern[i-m:].startswith(towel) else 0
        options.append(dp[n])
    return sum(options)


print(f"part 1: {part1()}")
print(f"part 2: {part2(patterns, towels)}")
