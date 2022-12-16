import itertools
import re

from lib import load_input


def solve(data, part=1):
    lines = data.splitlines()
    if part == 1:
        return part_one(lines)
    elif part == 2:
        return part_two(lines)


def part_one(data):
    y = 2000000
    pattern = re.compile(r"""Sensor at x=(?P<x_sensor>.*?), y=(?P<y_sensor>.*?): closest beacon is at x=(?P<x_beacon>.*?), y=(?P<y_beacon>.*?)$""")
    set1 = set()
    set2 = set()
    for line in data:
        match = pattern.match(line)
        sensor = (int(match.group("x_sensor")), int(match.group("y_sensor")))
        beacon = (int(match.group("x_beacon")), int(match.group("y_beacon")))
        if beacon[1] == y:
            set2.add(beacon[0])
        manhattan_distance = abs(sensor[0] - beacon[0]) + abs(sensor[1] - beacon[1])
        if sensor[1] - manhattan_distance <= y <= sensor[1] + manhattan_distance:
            for i in range(manhattan_distance - abs(y - sensor[1]) + 1):
                if sensor[0] + i not in set2:
                    set1.add(sensor[0] + i)
                if sensor[0] - i not in set2:
                    set1.add(sensor[0] - i)
    return len(set1)


def part_two(data):
    pattern = re.compile(
        r"""Sensor at x=(?P<x_sensor>.*?), y=(?P<y_sensor>.*?): closest beacon is at x=(?P<x_beacon>.*?), y=(?P<y_beacon>.*?)$""")
    datas = []
    beacons = []
    sensors = []
    manhattan_distances = []
    for line in data:
        match = pattern.match(line)
        sensor = (int(match.group("x_sensor")), int(match.group("y_sensor")))
        beacon = (int(match.group("x_beacon")), int(match.group("y_beacon")))
        manhattan_distance = abs(sensor[0] - beacon[0]) + abs(sensor[1] - beacon[1])
        beacons.append(beacon)
        sensors.append(sensor)
        manhattan_distances.append(manhattan_distance)
        datas.append((sensor, beacon, manhattan_distance))
    for cur in itertools.permutations(range(len(datas)), 4):
        a = sensors[cur[0]][1] - manhattan_distances[cur[0]] - sensors[cur[0]][0]
        b = sensors[cur[1]][1] - sensors[cur[1]][0] + manhattan_distances[cur[1]]
        c = sensors[cur[2]][0] - manhattan_distances[cur[2]] + sensors[cur[2]][1]
        d = sensors[cur[3]][0] + sensors[cur[3]][1] + manhattan_distances[cur[3]]
        if abs(a-b) == 2 and abs(c-d) == 2:
            a = [(sensors[cur[0]][0] + i, sensors[cur[0]][1] - manhattan_distances[cur[0]] + i) for i in
                 range(manhattan_distances[cur[0]] + 1)]
            c = [(sensors[cur[2]][0] - manhattan_distances[cur[2]] + i, sensors[cur[2]][1] - i) for i in
                 range(manhattan_distances[cur[2]] + 1)]
            a_mapped = [(a_1[0] + 1, a_1[1]) for a_1 in a]
            c_mapped = [(a_1[0] - 1, a_1[1]) for a_1 in c]
            result = set(a_mapped).intersection(c_mapped)
            if len(result) != 0:
                result = result.pop()
                flag = True
                for i in range(len(beacons)):
                   if abs(sensors[i][0] - result[0]) + abs(sensors[i][1] - result[1]) < manhattan_distances[i]:
                       flag = False
                if flag:
                    return 4000000 * result[0] + result[1]


if __name__ == "__main__":
    print(solve(load_input("small")))
    print(solve(load_input()))
    print(solve(load_input("small"), 2))
    print(solve(load_input(), 2))
