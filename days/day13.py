from functools import cmp_to_key

from lib import load_input


def solve(data, part=1):
    lines = data.split("\n\n")
    lines2 = [x for x in data.split("\n") if x]
    if part == 1:
        return part_one(lines)
    elif part == 2:
        return part_two(lines2)


def part_one(data):
    result = 0
    for i, lines in enumerate(data):
        l1,l2 = [eval(x) for x in lines.split('\n')]
        cur = compare(l1, l2)
        if cur > 0:
            result += i + 1
    return result


def compare(x, y):
    if isinstance(x, int) and isinstance(y, int):
        return y - x
    if isinstance(x, list) and isinstance(y, list):
        for j in range(max(len(x), len(y))):
            if j >= len(x):
                return 1
            elif j >= len(y):
                return -1
            cur = compare(x[j],y[j])
            if cur != 0:
                return cur
        return 0
    if isinstance(x, list):
        return compare(x, [y])
    else:
        return compare([x], y)

def part_two(data):
    lines_list = [[[2]], [[6]]]
    for line in data:
        lines_list.append(eval(line))
    sorted_list = sorted(lines_list, key=cmp_to_key(compare), reverse=True)
    result = 1
    for j, x in enumerate(sorted_list):
        if x == [[2]] or x == [[6]]:
            result *= j + 1
    return result


if __name__ == "__main__":
    # print(solve(load_input("small")))
    # print(solve(load_input()))
    print(solve(load_input("small"), 2))
    print(solve(load_input(), 2))
