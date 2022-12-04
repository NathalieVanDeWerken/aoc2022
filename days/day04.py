from lib import load_input


def solve(data, part=1):
    lines = data.splitlines()
    if part == 1:
        return part_one(lines)
    elif part == 2:
        return part_two(lines)


def part_one(data):
    score = 0
    for line in data:
        elf1, elf2 = line.split(",")
        elf1_min, elf1_max = [int(x) for x in elf1.split("-")][:2]
        elf2_min, elf2_max = [int(x) for x in elf2.split("-")][:2]
        if elf1_min <= elf2_min and elf1_max >= elf2_max or elf2_min <= elf1_min and elf2_max >= elf1_max:
            score += 1
    return score


def part_two(data):
    score = 0
    for line in data:
        elf1, elf2 = line.split(",")
        elf1_min, elf1_max = [int(x) for x in elf1.split("-")][:2]
        elf2_min, elf2_max = [int(x) for x in elf2.split("-")][:2]
        if elf1_min <= elf2_min <= elf1_max or elf2_min <= elf1_min <= elf2_max:
            score += 1
    return score


if __name__ == "__main__":
    print(solve(load_input("small")))
    print(solve(load_input()))
    print(solve(load_input("small"), 2))
    print(solve(load_input(), 2))
