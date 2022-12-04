def solve():
    p1_count = 0
    p2_count = 0
    with open("../inputs/day4.txt") as f:
        for line in f:
            s1,s2 = line.strip().split(",")
            elf1 = list(map(int,s1.split("-")))
            elf2 = list(map(int, s2.split("-")))

            # Check for enveloping overlap
            if elf1[0] <= elf2[0] and elf1[1] >= elf2[1]:
                p1_count += 1
            elif elf2[0] <= elf1[0] and elf2[1] >= elf1[1]:
                p1_count += 1

            # Check for any overlap
            r1 = list(range(elf1[0],elf1[1]+1))
            r2 = list(range(elf2[0], elf2[1] + 1))

            if not set(r1).isdisjoint(r2):
                p2_count += 1




    print("Part 1: ",p1_count)
    print("Part 2: ",p2_count)

if __name__ == "__main__":
    solve()