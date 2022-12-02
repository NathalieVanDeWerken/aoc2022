from lib import load_input


def solve(data, part=1):
    lines = data.splitlines()
    if part == 1:
        return part_one(lines)
    elif part == 2:
        return part_two(lines)


def part_one(data):
    score = 0
    print(data)
    for round in data:
        opponent, you = round.strip().split(" ")
        if you == "Y":
            score += 2
        elif you == "X":
            score += 1
        else:
            score += 3
        if (you == "Y" and opponent == "A") or (you == "Z" and opponent == "B") or (you == "X" and opponent == "C"):
            score += 6
        elif (you == "X" and opponent == "A") or (you == "Y" and opponent == "B") or (you == "Z" and opponent == "C"):
            score += 3
    return score


def part_two(data):
    score = 0
    for round in data:
        opponent, you = round.strip().split(" ")
        if you == "Y":
            score += 3
        elif you == "Z":
            score += 6
        if (you == "Y" and opponent == "A") or (you == "Z" and opponent == "C") or (you == "X" and opponent == "B"):
            score += 1
        elif (you == "X" and opponent == "C") or (you == "Z" and opponent == "A") or (you == "Y" and opponent == "B"):
            score += 2
        else:
            score += 3
    return score


if __name__ == "__main__":
    print(solve(load_input("small")))
    print(solve(load_input()))
    # print(solve(load_input("small"), 2))
    # print(solve(load_input(), 2))
