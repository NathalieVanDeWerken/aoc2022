from lib import load_input


def solve(data, part=1):
    lines = data
    if part == 1:
        return part_one(lines)
    elif part == 2:
        return part_two(lines)


def part_one(data):
    for i in range (4, len(data)):
        cur = set(x for x in data[i-4:i])
        if len(cur) == 4:
            return i


def part_two(data):
    for i in range(14, len(data)):
        cur = set(x for x in data[i - 14:i])
        if len(cur) == 14:
            return i


if __name__ == "__main__":
    print(solve(load_input("small")))
    print(solve(load_input()))
    print(solve(load_input("small"), 2))
    print(solve(load_input(), 2))
