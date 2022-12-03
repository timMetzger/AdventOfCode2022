def solve():
    with open("../inputs/day3.txt") as f:
        storage = []
        for line in f:
            r = []
            for c in line.strip():
                if 65 <= ord(c) <= 90:
                    r.append(ord(c) - 64 + 26)
                elif 97 <= ord(c) <= 122:
                    r.append(ord(c) - 96)
                else:
                    print("uhoh")

            storage.append(r)


    # Part 1
    total = 0
    for compartment in storage:
        c1 = compartment[:len(compartment)//2]
        c2 = compartment[len(compartment) // 2:]

        shared = set(c1).intersection(c2)

        if shared:
            total += shared.pop()

    print("Part 1: ", total)

    # Part 2
    total = 0
    i = 0
    while i < len(storage):
        r1 = storage[i]
        r2 = storage[i+1]
        r3 = storage[i+2]

        # Need element that is shared by all three compartments
        shared = set(r1).intersection(r2).intersection(r3)

        if shared:
            total += shared.pop()

        i += 3

    print("Part 2: ",total)
if __name__ == "__main__":
    solve()