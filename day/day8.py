from functools import reduce
def solve():
    with open("../inputs/day8.txt") as f:
        trees = [list(map(int,[*(line.strip())])) for line in f]


    # Part 1
    visible_count = 0
    visible_count += len(trees[0])*2 + (len(trees)-2) * 2
    visited = [[0]*len(trees[0]) for _ in range(len(trees))]
    for i in range(len(trees[0])):
        visited[0][i] = 1
        visited[len(trees)-1][i] = 1
        visited[i][0] = 1
        visited[i][len(trees[0])-1] = 1

    start = (1,1)
    visited[1][1] = 1
    q = [start]
    neighbors = [(1,0),(-1,0),(0,1),(0,-1)]
    scenic_score = 0
    while q:
        i,j = q.pop(0)

        visible = []
        view_scores = []
        # Add new neighbors
        for dx,dy in neighbors:
            x,y = i+dx,j+dy
            if x < len(trees) and y < len(trees[0]):
                if not visited[x][y]:
                    visited[x][y] = 1
                    q.append((x, y))

            # Look ahead to check if visible
            vis = True
            count = 0
            while 0 <= x < len(trees) and 0 <= y < len(trees[0]):
                if trees[x][y] >= trees[i][j]:
                    vis = False
                    count += 1
                    break

                x += dx
                y += dy
                count += 1

            view_scores.append(count)
            visible.append(vis)

        new_score = reduce(lambda x,y:x*y,view_scores)
        if new_score > scenic_score:
            scenic_score = new_score

        if any(visible):
            visible_count += 1


    print("Part 1: ",visible_count)
    print("Part 2: ",scenic_score)

if __name__ == "__main__":
    solve()