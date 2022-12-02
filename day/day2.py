


def part1():
    # A/X == ROCK
    # B/Y == PAPER
    # C/Z == SCISSORS

    total_score = 0
    with open("../inputs/day2.txt") as f:
        for line in f:
            score = 0
            m1,m2 = line.strip().split(" ")

            # Move score
            if m2 == "X":
                score += 1
            elif m2 == "Y":
                score += 2
            elif m2 == "Z":
                score += 3

            # Win
            if m2 == "X" and m1 == "C":
                score += 6
            elif m2 == "Y" and m1 == "A":
                score += 6
            elif m2 == "Z" and m1 == "B":
                score += 6

            # Draw
            elif ord(m2)-23 == ord(m1): # This would probably be easier to do from the start but whatever
                score += 3

            # Loss
            else:
                score += 0


            total_score += score

    print("Part 1: ",total_score)

def part2():
    # X -> lose
    # Y -> draw
    # Z -> win

    total_score = 0
    with open("../inputs/day2.txt") as f:
        for line in f:
            score = 0
            m1, m2 = line.strip().split(" ")

            # Need to lose
            if m2 == "X":
                if m1 == "A":
                    score += 3
                elif m1 == "B":
                    score += 1
                elif m1 == "C":
                    score += 2

            # Need to draw
            elif m2 == "Y":
                score += 3
                if m1 == "A":
                    score += 1
                elif m1 == "B":
                    score += 2
                elif m1 == "C":
                    score += 3
            # Need to win
            elif m2 == "Z":
                score += 6
                if m1 == "A":
                    score += 2
                elif m1 == "B":
                    score += 3
                elif m1 == "C":
                    score += 1

            else:
                print("Invalid move: ",m2)

            total_score += score


    print("Part 2: ",total_score)


if __name__ == "__main__":
    part1()
    part2()