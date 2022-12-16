def part1(start,graph):
    score = 0
    rate = 0
    t = 0

    current = start
    total_nodes = len(graph)
    while t < 30:
        score += rate

        # Find the traversal cost for each node from current node
        traversal_value = {}
        of_interest = [key for key in graph.keys() if graph[key]['state'] == 0 and graph[key]['rate'] != 0]

        for node in of_interest:

            visited = {key:0 for key in graph.keys()}
            visited[current] = 1

            q = [(current, 0)]

            while q:
                pos,cost = q.pop(0)
                if pos == node:
                    traversal_value[node] = cost + 1
                    break

                for neighbor in graph[pos]['neighbors']:
                    if not visited[neighbor]:
                        q.append((neighbor,cost+1))
                        visited[neighbor] = 1




        # Select the node that provides the most value and fits within time constraint
        choice = of_interest[0]
        best_score = 0
        choices = list(traversal_value.items())

        # If key 1 is selected what is the opportunity cost
        for key1,cost1 in choices:
            for key2,cost2 in choices:
                if key1 == key2:
                    continue
                if cost1 >= cost2:
                    gain = graph[key1]['rate']
                    opportunity_cost = (cost1 - cost2+1)*graph[key2]['rate']

                    if opportunity_cost > gain:
                        if opportunity_cost > best_score:
                            best_score = opportunity_cost
                            choice = key2


        current = choice
        graph[current]['state'] = 1
        rate += graph[current]['rate']
        t += traversal_value[current]




        print()



    score += rate
    return score




def solve():
    time = 0
    rate = 0
    graph = {}
    with open("../inputs/day16.txt") as f:
        for line in f:
            line = line.strip().replace(";","").replace(",","").split(" ")
            graph[line[1]] = {'rate':int(line[4].split("=")[-1]),'state':0,'neighbors':[]}
            for i in range(len(line)-1,0,-1):
                if "valve" in line[i]:
                    break
                else:
                    graph[line[1]]['neighbors'].append(line[i])

    start = "AA"
    print("Part 1: ",part1(start,graph))




if __name__ == "__main__":
    solve()