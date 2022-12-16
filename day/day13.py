# Comparison rules
# 1: if both values are integers, the lower should come first
#    if left is larger -> incorrect
#    if equal continue to next value
# 2: if both values are lists, compare values like above
#    if left list runs out of values first -> correct
#    if right runs outs first -> incorrect
#    if lists are the same length and no comparison decides continue on
# 3: if exactly one value is an integer convert that to a list and retry

# 1 is valid
# -1 is invalid
# 0 is unknown
def compare_ints(a,b):
    if a < b:
        return 1
    elif a > b:
        return -1
    else:
        return 0


def compare_lists(a,b):
    valid = 0

    for i in range(len(a)):
        if i >= len(b):
            break

        if type(a[i]) == type(b[i]) == int:
            valid = compare_ints(a[i],b[i])
        elif type(a[i]) == list and type(b[i]) == list:
            valid = compare_lists(a[i],b[i])
        elif type(a[i]) == int and type(b[i]) == list:
            valid = compare_lists([a[i]],b[i])
        elif type(a[i]) == list and type(b[i]) == int:
            valid = compare_lists(a[i],[b[i]])

        if valid == 1 or valid == -1:
            break

    if not valid:
        if len(a) < len(b):
            valid = 1
        elif len(a) > len(b):
            valid = -1

    return valid

def solve():
    pairs = []
    correct = []
    with open("../inputs/day13.txt") as f:
        line = f.readline()
        while line != "":
            line = line.strip()
            pairs.append((eval(line),eval(f.readline().strip())))
            f.readline()
            line = f.readline()

    for k,pair in enumerate(pairs,start=1):
        a,b = pair
        if compare_lists(a,b) == 1:
            correct.append(k)

    print("Part 1: ",sum(correct))



    # Need to sort the pairs such that the whole list is valid
    packets = []
    for pair in pairs:
        packets.extend([*pair])


    packets.append([[2]])
    packets.append([[6]])

    # Naive approach would be to sort this using bubblesort
    while True:
        swap = False
        for i in range(len(packets) - 1):
            if compare_lists(packets[i],packets[i+1]) != 1:
                packets[i], packets[i+1] = packets[i+1],packets[i]
                swap = True

        if not swap:
            break


    print("Part 2: ",(packets.index([[2]])+1)*(packets.index([[6]])+1))
if __name__ == "__main__":
    solve()