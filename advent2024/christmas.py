with open("../input/christmas.txt", "r") as f:
    input_ = f.read()
    keys_and_locks = [x.split("\n") for x in input_.split("\n\n")]

keys, locks = [], []
for key_or_lock in keys_and_locks:
    if key_or_lock[0] == "#####":
        locks.append(key_or_lock)
    else:
        keys.append(key_or_lock)


def get_tumbler_and_key_heights(key_or_lock: list[str], is_lock: bool):
    heights = [0] * 5
    if not is_lock:
        key_or_lock = key_or_lock[::-1]
    for r, row in enumerate(key_or_lock):
        for c, col in enumerate(row):
            heights[c] += 1 if col == "#" else 0
    return heights


max_tumbler = len(locks[0])
fits = 0
for lock in locks:
    tumbler_heights = get_tumbler_and_key_heights(lock, True)
    for key in keys:
        key_heights = get_tumbler_and_key_heights(key, False)
        fits += 1 if all(tumbler_heights[i] + key_heights[i] <= max_tumbler for i in range(len(tumbler_heights))) else 0

print(f"part 1: {fits}")
