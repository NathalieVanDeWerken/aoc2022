from lib import load_input


def solve(data, part=1):
    lines = [[int(y) for y in x] for x in data.splitlines()]
    if part == 1:
        return part_one(lines)
    elif part == 2:
        return part_two(lines)


def part_one(data):
    print(data)
    count = 0
    for x  in range(len(data)):
        for y in range(len(data[x])):
            if all(data[x][y_2] < data[x][y] for y_2 in range(y+1, len(data[x]))) or\
                    all(data[x][y_2] < data[x][y] for y_2 in range(0, y)) or\
                    all(data[x_2][y] < data[x][y] for x_2 in range(x+1, len(data))) or\
                    all(data[x_2][y] < data[x][y] for x_2 in range(0, x)):
                count += 1
    return count


def part_two(data):
    result = 0
    for x  in range(len(data)):
        for y in range(len(data[x])):
            left =  y - next((index for index in range(y-1, 0, -1) if data[x][index] >= data[x][y]), 0)
            right = next((index for index in range(y+1, len(data[x]) - 1) if data[x][index] >= data[x][y]), len(data) - 1) - y
            up = x - next((index for index in range(x - 1, 0, -1) if data[index][y] >= data[x][y]), 0)
            down = next((index for index in range(x+1, len(data) - 1) if data[index][y] >= data[x][y]), len(data) - 1) - x
            result = max(result, left * right * up * down)
    return result



if __name__ == "__main__":
    # print(solve(load_input("small")))
    # print(solve(load_input()))
    print(solve(load_input("small"), 2))
    print(solve(load_input(), 2))
