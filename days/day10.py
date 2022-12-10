from lib import load_input


def solve(data, part=1):
    lines = data.splitlines()
    if part == 1:
        return part_one(lines)
    elif part == 2:
        return part_two(lines)


def part_one(data):
    result = 0
    x = 1
    cycle = 0
    for line in data:
        if line == "noop":
            cycle += 1
            result += check_update(cycle, x)
        else:
            cycle += 1
            result += check_update(cycle, x)
            cycle += 1
            result += check_update(cycle, x)
            x += int(line.split(" ")[1])

    return result

def check_update(cycle, x):
    if cycle % 40 == 20:
        return x * cycle
    else:
        return 0

def part_two(data):
    result = []
    x = 1
    cycle = 0
    cur = ""
    for line in data:
        if line == "noop":
            cur += draw(x, cycle)
            cycle += 1
            if len(cur) == 40:
                result.append(cur)
                cur = ""
                cycle = 0
        else:
            cur += draw(x, cycle)
            cycle += 1
            if len(cur) == 40:
                result.append(cur)
                cur = ""
                cycle = 0
            cur += draw(x, cycle)
            cycle += 1
            if len(cur) == 40:
                result.append(cur)
                cur = ""
                cycle = 0
            x += int(line.split(" ")[1])
    return result


def draw(x, cycle):
    if abs(x - cycle) <= 1:
        return "#"
    else:
        return "."


if __name__ == "__main__":
    print(solve(load_input("small")))
    print(solve(load_input()))
    for x in solve(load_input(), 2):
        print(x)
