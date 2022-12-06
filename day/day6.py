def solve():
    sequence = ""
    with open("../inputs/day6.txt") as f:
        sequence = f.readline().strip()

    left = 0
    right = 3
    while right < len(sequence):
        if len(set(sequence[left:right+1])) == 4:
            print("Part 1: ",right+1)
            break

        left += 1
        right += 1

    left = 0
    right = 13
    while right < len(sequence):
        if len(set(sequence[left:right+1])) == 14:
            print("Part 2: ",right+1)
            break

        left += 1
        right += 1




if __name__ == "__main__":
    solve()