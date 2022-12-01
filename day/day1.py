def part1():
    cal_counts = {}
    with open("../inputs/day1_1.txt") as f:
        total = 0
        elf = 1
        for line in f:
            if line == "\n":
                cal_counts[elf] = total
                total = 0
                elf += 1
            else:
                total += int(line.strip())

    cals = list(cal_counts.values())
    cals.sort()
    print("Part 1: ",cals[-1])
    print("Part 2: ",sum(cals[-3:]))




if __name__ == "__main__":
    part1()