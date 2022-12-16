def solve():
    walls = []
    with open("../inputs/day14.txt") as f:
        for line in f:
            line = line.strip().split(" -> ")
            segment = [list(map(int,s.split(","))) for s in line]
            walls.append(segment)

    obstacles = set()
    max_y = 0
    for wall in walls:
        for i in range(len(wall)-1):
            x1,y1 = wall[i]
            x2,y2 = wall[i+1]
            if y1 > max_y:
                max_y = y1
            if y2 > max_y:
                max_y = y2

            if x1 == x2:
                l = max(y1,y2)
                s = min(y1,y2)
                obstacles.update(set([(x1,y) for y in range(s,l+1)]))

            if y1 == y2:
                l = max(x1,x2)
                s = min(y1,y2)
                obstacles.update(set([(x,y1) for x in range(s,l+1)]))

    obstacles.update(set((i, max_y+2) for i in range(490-(max_y),510+(max_y))))

    wall_count = len(obstacles)
    start = (500, 0)

    part1_done = False
    part2_done = False
    while not part2_done:
        x,y = start
        while True:
            if (x,y+1) not in obstacles:
                y +=1
            elif (x-1,y+1) not in obstacles:
                x -= 1
                y += 1
            elif (x+1,y+1) not in obstacles:
                x += 1
                y += 1
            else:
                if y == max_y + 1 and not part1_done:
                    print("Part 1: ",len(obstacles) - wall_count)
                    part1_done = True

                obstacles.add((x,y))
                if (x,y) == start:
                    print("Part 2: ", len(obstacles) - wall_count)
                    part2_done = True
                    break
                break






if __name__ == "__main__":
    solve()