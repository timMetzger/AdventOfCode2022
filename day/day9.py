neighbors = [(1,0),(-1,0),(0,1),(0,-1),(1,1),(-1,1),(1,-1),(-1,-1)]
def touching(head,tail):
    if head == tail:
        return True
    else:

        for dx,dy in neighbors:
            x = [head[0]+dx,head[1]+dy]
            if x == tail:
                return True

        return False

def move_tail(head,tail):
    # Have to separate the diagonal logic so that counting occurs correctly
    # as there are scenario where moving diagonally is to make the head and tail
    # touch is not the correct movement despite it producing the proper result

    # Need to move diagonally
    if head[0] != tail[0] and head[1] != tail[1]:
        for dx,dy in neighbors[4:]:
            x = [tail[0]+dx,tail[1]+dy]
            if touching(head,x):
                tail[0] += dx
                tail[1] += dy
                break
    # Need to move left,right,up,down
    else:
        for dx,dy in neighbors[:4]:
            x = [tail[0]+dx,tail[1]+dy]
            if touching(head,x):
                tail[0] += dx
                tail[1] += dy
                break

def update_chain(knots):
    i = 0
    while i < len(knots)-1:
        head = knots[i]
        tail = knots[i+1]
        if not touching(head,tail):
            move_tail(head,tail)

        i += 1

def solve():
    KNOTS = 10
    visited = set()
    knots = [[0,0] for _ in range(KNOTS)]
    visited.add(tuple(knots[-1]))

    with open("../inputs/day9.txt") as f:
        for line in f:
            direction, distance = line.strip().split(" ")
            distance = int(distance)


            if direction == "R":
                while distance > 0:
                    knots[0][1] += 1
                    update_chain(knots)
                    visited.add(tuple(knots[-1]))
                    distance -= 1

            elif direction == "L":
                while distance > 0:
                    knots[0][1] -= 1
                    update_chain(knots)
                    visited.add(tuple(knots[-1]))
                    distance -= 1

            elif direction == "U":
                while distance > 0:
                    knots[0][0] += 1
                    update_chain(knots)
                    visited.add(tuple(knots[-1]))
                    distance -= 1

            elif direction == "D":
                while distance > 0:
                    knots[0][0] -= 1

                    update_chain(knots)
                    visited.add(tuple(knots[-1]))
                    distance -= 1

    print("Part 2: ",len(visited))



if __name__ == "__main__":
    solve()

