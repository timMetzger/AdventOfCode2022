from itertools import groupby

def manhattan_dist(p1,p2):
    return abs(p1[0]-p2[0]) + abs(p1[1]-p2[1])

def solve():
    sensors = set()
    beacons = set()
    coverage = set()
    sensor_perimeter = {}

    row = 2000000
    max_xy = 4000000


    with open("../inputs/day15.txt") as f:
        for line in f:
            line = line.strip().replace(":","").replace(",","").split(" ")
            sx = int(line[2].split("=")[1])
            sy = int(line[3].split("=")[1])
            bx = int(line[8].split("=")[1])
            by = int(line[9].split("=")[1])

            sensors.add((sx,sy))
            beacons.add((bx,by))




            s = (sx,sy)
            max_dist = manhattan_dist(s,(bx,by))

            p = (sx, row)
            while manhattan_dist(s, p) < max_dist:
                p = (p[0] - 1, row)
            min_x = p[0]

            p = (sx, row)
            while manhattan_dist(s, p) < max_dist:
                p = (p[0] + 1, row)
            max_x = p[0]

            min_y = sy - max_dist
            max_y = sy + max_dist

            lines = set()
            lines.add((min_x, sy, sx, min_y))
            lines.add((max_x, sy, sx, min_y))
            lines.add((min_x, sy, sx, max_y))
            lines.add((max_x, sy, sx, max_y))

            sensor_perimeter[s] = set(lines)


            if sy + max_dist >= row or sy - max_dist <= row:

                for x in range(min_x,max_x+1):
                    if manhattan_dist(s,(x,row)) <= max_dist:
                        coverage.add((x,row))




    # Part 1
    count = 0
    for p in coverage:
        if p[1] == row:
            count += 1

    for s in sensors:
        if s[1] == row:
            count -= 1

    for b in beacons:
        if b[1] == row:
            count -= 1
    print("Part 1: ",count)


    # Part 2
    # going to try taking the expanded perimeter of each sensor and seeing if all
    # points


if __name__ == "__main__":
    solve()