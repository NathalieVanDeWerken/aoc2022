from lib import load_input


def solve(data, part=1):
    lines = data
    if part == 1:
        return part_one(lines)
    elif part == 2:
        return part_two(lines)


def part_one(data):
    stacks, operations = parse_data(data)
    for operation in operations:
        for _ in range(operation[0]):
            stacks[operation[2] - 1].append(stacks[operation[1] - 1].pop())
    result = ""
    for stack in stacks:
        result += stack.pop()
    return result


def parse_data(data):
    raw_stacks, raw_operations = data.split("\n\n")
    raw_stacks = raw_stacks.split("\n")
    number_of_stacks = int(raw_stacks[-1].strip().split(" ")[-1])
    stacks = []

    for _ in range(number_of_stacks):
        stacks.append([])

    for i in range(number_of_stacks):
        for j in range(len(raw_stacks) - 2, -1, -1):
            if len(raw_stacks[j]) <= 2 + i * 4 or raw_stacks[j][1 + i * 4] == " ":
                continue
            stacks[i].append(raw_stacks[j][1 + i * 4])
    all_operations = []
    for line in raw_operations.split("\n"):
        single_operation = line.split(" ")
        all_operations.append((int(single_operation[1]), int(single_operation[3]), int(single_operation[5])))
    return stacks, all_operations


def part_two(data):
    stacks, operations = parse_data(data)
    for operation in operations:
        temp_list = []
        for _ in range(operation[0]):
            temp_list.append(stacks[operation[1] - 1].pop())
        temp_list.reverse()
        for x in temp_list:
            stacks[operation[2] - 1].append(x)
    result = ""
    for stack in stacks:
        result += stack.pop()
    return result


if __name__ == "__main__":
    print(solve(load_input("small")))
    print(solve(load_input()))
    print(solve(load_input("small"), 2))
    print(solve(load_input(), 2))
