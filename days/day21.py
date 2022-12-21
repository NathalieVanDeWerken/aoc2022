from lib import load_input


def solve(data, part=1):
    lines = data.splitlines()
    if part == 1:
        return part_one(lines)
    elif part == 2:
        return part_two(lines)


def part_one(data):
    operations = {}
    for line in data:
        line = line.split(": ")
        operations[line[0]] = line[1]
    return int(find_value(operations, 'root'))
    pass

def find_value(operations, value):
    operation = operations[value]
    if " " in operation:
        operation2 = operation.split(" ")
        value1 = find_value(operations, operation2[0])
        value2 = find_value(operations, operation2[2])
        return eval(operation, {operation2[0]: value1, operation2[2]: value2})
    else:
        return int(operation)

def part_two(data):
    operations = {}
    for line in data:
        line = line.split(": ")
        if line[0] == 'root':
            operations[line[0]] = line[1].replace("+", "=")
        else:
            operations[line[0]] = line[1]
    return find_value_2(operations, 'root')
    pass

def find_value_2(operations, value):
    operation = operations[value]
    if " " in operation:
        operation2 = operation.split(" ")
        value1 = find_value_2(operations, operation2[0])
        value2 = find_value_2(operations, operation2[2])
        return f"({value1} {operation2[1]} {value2})"
    else:
        if value == "humn":
            return "x"
        return operation


if __name__ == "__main__":
    # print(solve(load_input("small")))
    # print(solve(load_input()))
    print(solve(load_input("small"), 2))
    print(solve(load_input(), 2))
