def solve():
    cycle = 1
    x = 1
    signal_strengths = []
    marker = 20

    display = [[0]*40for _ in range(6)]
    i = 0
    j = 0
    with open("../inputs/day10.txt") as f:
        for line in f:
            line = line.strip().split(" ")

            if len(line) == 2:
                n = 0
                while n < 2:
                    n += 1
                    cycle += 1

                    # Draw to display
                    if x == j or j - 1 == x or j + 1 == x:
                        display[i][j] = "#"
                    else:
                        display[i][j] = "."

                    j += 1

                    # If it is end of cycle 2 need to add to register before signal strength
                    if n == 2:
                        x += int(line[1])

                    # Have to check cycles mid execution
                    if cycle == marker:
                        signal_strengths.append(cycle * x)
                        marker += 40

            else:
                # Draw to display
                if x == j or j - 1 == x or j + 1 == x:
                    display[i][j] = "#"
                else:
                    display[i][j] = "."

                j += 1

                cycle += 1


                if cycle == marker:
                    signal_strengths.append(cycle*x)
                    marker += 40


            # Move pointer to next row
            if j == 40:
                i += 1
                j = 0


    print("Part 1: ",sum(signal_strengths))
    print("Part 2:")
    for row in display:
        print("".join(row))


    # X register set the horizontal position of the middle of the sprite
    # Sprite starts at (0,0) and covers (0,-1) and (0,1)


if __name__ == "__main__":
    solve()