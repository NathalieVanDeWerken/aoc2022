import math

from lib import load_input


def solve(data, part=1):
    lines = data.splitlines()
    if part == 1:
        return part_one(lines)
    elif part == 2:
        return part_two(lines)


def part_one(data):
    head = (0,0)
    tail = (0,0)
    visited = set()
    visited.add(tail)
    for line in data:
        direction, amount = line.split()
        amount = int(amount)
        for _ in range(amount):
            head = move_head(direction, head)
            tail = move_tail(head, tail)
            visited.add(tail)
    return len(visited)


def part_two(data):
    coords = []
    for _ in range(10):
        coords.append((0,0))
    visited = set()
    visited.add(coords[9])
    for line in data:
        direction, amount = line.split()
        amount = int(amount)
        for _ in range(amount):
            coords[0] = move_head(direction, coords[0])
            for i in range(1,10):
                coords[i] = move_tail(coords[i-1], coords[i])
            visited.add(coords[9])
    return len(visited)

def move_head(direction, head):
    if direction == "R":
        head = (head[0] + 1, head[1])
    elif direction == "L":
        head = (head[0] - 1, head[1])
    elif direction == "U":
        head = (head[0], head[1] + 1)
    else:
        head = (head[0], head[1] - 1)
    return head


def move_tail(head, tail):
    if (abs(head[0] - tail[0])) <= 1 and abs(head[1] - tail[1]) <= 1:
        return tail
    if abs(head[0] - tail[0]) == 2 and abs(head[1] - tail[1]) == 1:
        tail = (tail[0] + (head[0] - tail[0]) // 2, head[1])
    elif abs(head[0] - tail[0]) == 1 and abs(head[1] - tail[1]) == 2:
        tail = (head[0], tail[1] + (head[1] - tail[1]) // 2)
    else:
        tail = (tail[0] + (head[0] - tail[0]) // 2, tail[1] + (head[1] - tail[1]) // 2)
    return tail


if __name__ == "__main__":
    print(solve(load_input("small")))
    print(solve(load_input()))
    print(solve(load_input("small"), 2))
    print(solve(load_input(), 2))
