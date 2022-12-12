from lib import load_input


def solve(data, part=1):
    lines = data.split("\n\n")
    if part == 1:
        return part_one(lines)
    elif part == 2:
        return part_two(lines)


def part_one(data):
    monkeys = parse_monkeys(data)
    result = [0] * len(monkeys)
    for _ in range(20):
        for i, monkey in enumerate(monkeys):
            for item in monkey[0]:
                result[i] += 1
                worry = eval(monkey[1], {"old": item})
                worry = worry // 3
                if worry % monkey[2] == 0:
                    monkeys[monkey[3]][0].append(worry)
                else:
                    monkeys[monkey[4]][0].append(worry)
            monkey[0].clear()
    result.sort()
    return result[-1] * result[-2]

def parse_monkeys(data):
    monkeys = []
    for monkey in data:
        lines = monkey.split("\n")
        items = [int(x) for x in lines[1].split(": ")[1].split(", ")]
        op = lines[2].split("= ")[1]
        divis_by = int(lines[3].split(" ")[-1])
        true_op = int(lines[4].split(" ")[-1])
        false_op = int(lines[5].split(" ")[-1])
        monkeys.append((items, op, divis_by, true_op, false_op))
    return monkeys


def part_two(data):
    monkeys = parse_monkeys(data)
    result = [0] * len(monkeys)
    to_mod = 1
    for monkey in monkeys:
        to_mod *= monkey[2]
    for x in range(10000):
        for i, monkey in enumerate(monkeys):
            for item in monkey[0]:
                result[i] += 1
                worry = eval(monkey[1], {"old": item})
                if worry % monkey[2] == 0:
                    monkeys[monkey[3]][0].append(worry % to_mod)
                else:
                    monkeys[monkey[4]][0].append(worry % to_mod)
            monkey[0].clear()
    result.sort()
    return result[-1] * result[-2]


if __name__ == "__main__":
    print(solve(load_input("small")))
    print(solve(load_input()))
    print(solve(load_input("small"), 2))
    print(solve(load_input(), 2))
