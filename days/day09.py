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
    head = (0,0)
    knot1= (0,0)
    knot2 = (0,0)
    knot3 = (0,0)
    knot4 = (0,0)
    knot5 = (0,0)
    knot6 = (0,0)
    knot7 = (0,0)
    knot8 = (0,0)
    knot9 = (0,0)
    visited = set()
    visited.add(knot9)
    for line in data:
        direction, amount = line.split()
        amount = int(amount)
        for _ in range(amount):
            head = move_head(direction, head)
            knot1 = move_tail(head, knot1)
            knot2 = move_tail(knot1, knot2)
            knot3 = move_tail(knot2, knot3)
            knot4 = move_tail(knot3, knot4)
            knot5 = move_tail(knot4, knot5)
            knot6 = move_tail(knot5, knot6)
            knot7 = move_tail(knot6, knot7)
            knot8 = move_tail(knot7, knot8)
            knot9 = move_tail(knot8, knot9)
            visited.add(knot9)
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
