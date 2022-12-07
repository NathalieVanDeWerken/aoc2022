from lib import load_input

class Node:
    def __init__(self, name, parent, size, is_dir):
        self.name = name
        self.parent = parent
        self.size = size
        self.children= []
        self.is_dir = is_dir


    def find_child(self, name):
        for child in self.children:
            if child.name == name:
                return child


def solve(data, part=1):
    lines = data.splitlines()
    if part == 1:
        return part_one(lines)
    elif part == 2:
        return part_two(lines)


def part_one(data):
    root = make_tree(data)
    calculate_sizes(root)
    return sum_part1(root)


def calculate_sizes(node):
    s = 0
    s += node.size
    for child in node.children:
        calculate_sizes(child)
        s += child.size
    node.size = s

def sum_part1(node):
    result = 0
    if node.size <= 100000 and node.is_dir:
        result += node.size
    for child in node.children:
        result += sum_part1(child)
    return result


def make_tree(data):
    root = Node("/", None, 0, True)
    current = root
    for line in data:
        # print(current)
        line = line.split(" ")
        if line[0] == "$":
            if line[1] == "cd":
                if line[2] == "/":
                    current = root
                elif line[2] == "..":
                    current = current.parent
                else:
                    current = current.find_child(line[2])
        else:
            if line[0] == "dir":
                current.children.append(Node(line[1], current, 0, True))
            else:
                current.children.append(Node(line[1], current, int(line[0]), False))
    return root


def part_two(data):
    root = make_tree(data)
    calculate_sizes(root)
    space_to_find =30000000 - (70000000 - root.size)
    all_sizes = find_all_sizes(root)
    viable = list(filter(lambda x : x >= space_to_find, all_sizes))
    viable.sort()
    return viable[0]


def find_all_sizes(node):
    result = []
    if node.is_dir:
        result.append(node.size)
        for child in node.children:
            result.extend(find_all_sizes(child))
    return result


if __name__ == "__main__":
    print(solve(load_input("small")))
    print(solve(load_input()))
    print(solve(load_input("small"), 2))
    print(solve(load_input(), 2))
