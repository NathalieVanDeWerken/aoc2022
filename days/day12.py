import sys

from lib import load_input


def solve(data, part=1):
    lines = [list(x) for x in data.splitlines()]
    if part == 1:
        return part_one(lines)
    elif part == 2:
        return part_two(lines)


def part_one(data):
    return bfs(data, find_starting_point(data))


def find_starting_point(data):
    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] == "S":
                return i, j
    return None


def can_visit(new, old, data):
    if 0 <= new[0] < len(data) and 0 <= new[1] < len(data[new[0]]):
        if data[new[0]][new[1]] == 'E':
            return data[old[0]][old[1]] == "y" or data[old[0]][old[1]] == "z"
        if data[old[0]][old[1]] == 'S':
            return data[new[0]][new[1]] == "a" or data[new[0]][new[1]] == "b"
        return ord(data[new[0]][new[1]]) - ord(data[old[0]][old[1]]) <= 1
    return False


def bfs(data, start_point):
    visited = set()
    to_visit = []
    dirs = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    to_visit.append((start_point, 0))
    while len(to_visit) != 0:
        visiting, lvl = to_visit.pop(0)
        if visiting in visited:
            continue
        # print(visiting, data[visiting[0]][visiting[1]])
        visited.add(visiting)
        if (data[visiting[0]][visiting[1]]) == "E":
            return lvl
        for i in dirs:
            new_coor = (visiting[0] + i[0], visiting[1] + i[1])
            if can_visit(new_coor, visiting, data):
                to_visit.append((new_coor, lvl + 1))
    return sys.maxsize


def part_two(data):
    starting_points = find_starting_points(data)
    result = sys.maxsize
    for start_point in starting_points:
        result = min(result, bfs(data, start_point))
    return result


def find_starting_points(data):
    result = []
    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] == "S" or data[i][j] == "a":
                result.append((i, j))
    return result


if __name__ == "__main__":
    print(solve(load_input("small")))
    print(solve(load_input()))
    print(solve(load_input("small"), 2))
    print(solve(load_input(), 2))
