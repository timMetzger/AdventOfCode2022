import queue
from copy import deepcopy

def dijkstra(start,goal,height_map,dist,parents,visited):
    neighbors = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    q = queue.PriorityQueue()
    dist[start] = 0
    q.put((dist[start], start))

    shortest_a = None

    while q.qsize() > 0:
        current = q.get()
        current_score = current[0]
        i,j = current[1]

        visited[(i, j)] = True

        if height_map[i][j] == ord('a') and shortest_a is None:
            shortest_a = current[1]

        if current[1] == goal:
            break

        for dx, dy in neighbors:
            x = i + dx
            y = j + dy
            if 0 <= x < len(height_map) and 0 <= y < len(height_map[0]) and not visited[(x,y)]:
                if -150 <= height_map[i][j] - height_map[x][y] <= 1: # movement down in elevation is unlimited
                    temp = dist[(i,j)] + 1
                    if temp < dist[(x,y)]:
                        dist[(x,y)] = temp
                        parents[(x,y)] = (i,j)
                        q.put((dist[(x,y)],(x,y)))


    path = []
    current = parents[goal]
    while current is not None:
        path.append(current)
        current = parents[current]

    print("Part 1: ",len(path))

    path = []
    current = parents[shortest_a]
    while current is not None:
        path.append(current)
        current = parents[current]

    print("Part 2: ",len(path))

def solve():
    start_code = ord("S")
    end_code = ord("E")
    with open("../inputs/day12.txt") as f:
        height_map = [list(map(ord,line.strip())) for line in f]


    start = None
    goal = None

    for i,row in enumerate(height_map):
        if start_code in row:
            j = row.index(start_code)
            start = (i,j)
            height_map[i][j] = ord("a")
        if end_code in row:
            j = row.index(end_code)
            goal = (i,j)
            height_map[i][j] = ord("z")



    dist = {}
    parents = {}
    visited = {}
    q = queue.PriorityQueue()
    for i in range(len(height_map)):
        for j in range(len(height_map[0])):
            dist[(i,j)] = float('inf')
            parents[(i,j)] = None
            visited[(i,j)] = False


    dijkstra(goal,start,height_map,deepcopy(dist),deepcopy(parents),deepcopy(visited))







if __name__ == "__main__":
    solve()