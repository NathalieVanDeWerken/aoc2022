from lib import load_input


def solve(data, part=1):
    lines = data.splitlines()
    if part == 1:
        return part_one(lines)
    elif part == 2:
        return part_two(lines)


def part_one(data):
    score = 0
    for rucksack in data:
        part1 = set()
        part2 = set()
        for i in range(len(rucksack) // 2):
            part1.add(rucksack[i])
            part2.add(rucksack[i + len(rucksack) // 2])
        score += calc_score(part1.intersection(part2))
    return score


def calc_score(entry):
    for value in entry:
        if value.islower():
            return ord(value) - 96
        return ord(value) - 64 + 26


def part_two(data):
    score = 0
    for i in range(0, len(data), 3):
        part1 = set()
        part2 = set()
        part3 = set()
        for j in data[i]:
            part1.add(j)
        for j in data[i + 1]:
            part2.add(j)
        for j in data[i + 2]:
            part3.add(j)
        score += calc_score(part1.intersection(part2).intersection(part3))
    return score


if __name__ == "__main__":
    # print(solve(load_input("small")))
    # print(solve(load_input()))
    print(solve(load_input("small"), 2))
    print(solve(load_input(), 2))
