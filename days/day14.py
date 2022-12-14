from lib import load_input


def solve(data, part=1):
    lines = data.splitlines()
    if part == 1:
        return part_one(lines)
    elif part == 2:
        return part_two(lines)


def part_one(data):
    floor = 0
    ground = set()
    for line in data:
        line = [[int(y) for y in x.split(",")] for x in line.split(" -> ")]
        init = line[0]
        for next in line[1:]:
            dx, dy = [el2 - el1 for(el1, el2) in zip(init, next)]
            ground.add((init[0], init[1]))
            if dx > 0:
                for i in range(dx + 1):
                    ground.add((init[0] + i, init[1]))
            elif dx < 0:
                for i in range(-dx + 1):
                    ground.add((init[0] - i, init[1]))
            elif dy > 0:
                for i in range(dy + 1):
                    ground.add((init[0], init[1] + i))
            else:
                for i in range(-dy + 1):
                    ground.add((init[0], init[1] - i))
            init = next
    for x in ground:
        floor = max(floor, x[1])
    result = 0
    while True:
        sand_coor_x = 500
        sand_coor_y = 0
        while True:
            print(sand_coor_x, sand_coor_y)
            sand_coor_y += 1
            if (sand_coor_x, sand_coor_y) not in ground:
                print("hey")
            elif (sand_coor_x -1, sand_coor_y) not in ground:
                print("hi")
                sand_coor_x -= 1
            elif (sand_coor_x +1 , sand_coor_y) not in ground:
                print("ho")
                sand_coor_x += 1
            else:
                print("no")
                ground.add((sand_coor_x, sand_coor_y - 1))
                result += 1
                break
            if sand_coor_y > floor:

                return result



def part_two(data):
    floor = 0
    ground = set()
    for line in data:
        line = [[int(y) for y in x.split(",")] for x in line.split(" -> ")]
        init = line[0]
        for next in line[1:]:
            dx, dy = [el2 - el1 for (el1, el2) in zip(init, next)]
            ground.add((init[0], init[1]))
            if dx > 0:
                for i in range(dx + 1):
                    ground.add((init[0] + i, init[1]))
            elif dx < 0:
                for i in range(-dx + 1):
                    ground.add((init[0] - i, init[1]))
            elif dy > 0:
                for i in range(dy + 1):
                    ground.add((init[0], init[1] + i))
            else:
                for i in range(-dy + 1):
                    ground.add((init[0], init[1] - i))
            init = next
    for x in ground:
        floor = max(floor, x[1])
    result = 0
    while True:
        sand_coor_x = 500
        sand_coor_y = 0
        while True:
            # print(sand_coor_x, sand_coor_y)
            sand_coor_y += 1
            if sand_coor_y >= floor + 2:
                ground.add((sand_coor_x, sand_coor_y - 1))
                result += 1
                break
            elif (sand_coor_x, sand_coor_y) not in ground:
                pass
            elif (sand_coor_x - 1, sand_coor_y) not in ground:
                sand_coor_x -= 1
            elif (sand_coor_x + 1, sand_coor_y) not in ground:
                sand_coor_x += 1
            else:
                ground.add((sand_coor_x, sand_coor_y - 1))
                if sand_coor_x == 500 and sand_coor_y - 1 == 0:
                    return result + 1
                result += 1
                break



if __name__ == "__main__":
    print(solve(load_input("small")))
    print(solve(load_input()))
    print(solve(load_input("small"), 2))
    print(solve(load_input(), 2))
