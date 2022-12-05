# Block world problem but all steps are given
import copy


def parse_input():
    NUM_STACKS = 9
    stacks = [[] for _ in range(NUM_STACKS)]
    instructions = []
    with open("../inputs/day5.txt") as f:
        for line in f:
            i = 1
            j = 0
            if line != "\n":
                # Grab initial stack configuration
                if not line[i].isnumeric():
                    while i < len(line):
                        if line[i].isalpha():
                            stacks[j].append(line[i])

                        i += 4
                        j += 1

            else:
                break

        # Read in intruction set
        for line in f:
            line = line.strip().split(" ")
            instructions.append((int(line[3])-1,int(line[5])-1,int(line[1])))

    return stacks, instructions


def solve():

    # Instructions are tuples of (src,dest,qty)
    stacks,instructions = parse_input()
    stacks_copy = copy.deepcopy(stacks)

    # Solve Part 1
    for command in instructions:
        src,dest,qty = command

        for _ in range(qty):
            stacks[dest].insert(0,stacks[src].pop(0))

    # Get top block from each stack
    part1 = ""
    for stack in stacks:
        if stack:
            part1 += stack[0]

    print("Part 1: ",part1)

    # Solve part 2
    for command in instructions:
        src, dest, qty = command
        to_move = stacks_copy[src][:qty]

        for _ in range(qty):
            stacks_copy[src].pop(0)
            stacks_copy[dest].insert(0,to_move.pop())


    # Get top block from each stack
    part2 = ""
    for stack in stacks_copy:
        if stack:
            part2 += stack[0]

    print("Part 2: ",part2)

if __name__ == "__main__":
    solve()