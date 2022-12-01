from lib import load_input


def solve(data, part=1):
    lines = data.splitlines()
    if part == 1:
        return part_one(lines)
    elif part == 2:
        return part_two(lines)


def part_one(data):
    maximum = 0
    current = 0
    for x in data:
        if x == '':
            maximum = max(current, maximum)
            current = 0
        else:
            current += int(x)
    maximum = max(current, maximum)
    return maximum


def part_two(data):
    all_elves = []
    current = 0
    for x in data:
        if x == '':
            all_elves.append(current)
            current = 0
        else:
            current += int(x)
    all_elves.append(current)
    return sum(sorted(all_elves, reverse=True)[:3])

if __name__ == "__main__":
    print(solve(load_input("small")))
    # print(solve(load_input()))
    # print(solve(load_input("small"), 2))
    # print(solve(load_input(), 2))
