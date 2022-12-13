# Comparison rules
# 1: if both values are integers, the lower should come first
#    if left is larger -> incorrect
#    if equal continue to next value
# 2: if both values are lists, compare values like above
#    if left list runs out of values first -> correct
#    if right runs outs first -> incorrect
#    if lists are the same length and no comparison decides continue on
# 3: if exactly one value is an integer convert that to a list and retry


def compare_lists(a,b):
    if len(b) == len(a) == 0:
        return False

    # if len(a) > 0 and type(a[0]) == list:
    #     return compare_lists(a[0],b)
    # elif len(b) > 0 and type(b[0]) == list:
    #     return compare_lists(a, b[0])


    if len(b) > 0 and len(a) == 0:
        return True



    for i in range(len(a)):
        if i >= len(b):
            return False

        if type(a[i]) == type(b[i]) == int:
            if a[i] > b[i]:
                return False
            elif a[i] < b[i] and i == len(b)-1:
                return True
        elif type(a[i]) == type(b[i]) == list:
            if not compare_lists(a[i],b[i]):
                return False
        elif type(a[i]) == int and type(b[i]) == list:
            if not compare_lists([a[i]],b[i]):
                return False
        elif type(a[i]) == list and type(b[i]) == int:
            if not compare_lists(a[i],[b[i]]):
                return False


    return True

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
        correct_flag = True
        a = pair[0]
        b = pair[1]
        for i in range(len(pair[0])):
            if i >= len(b):
                correct_flag = False
                break

            if type(a[i]) == int and type(b[i]) == list:
                if not compare_lists([a[i]],b[i]):
                    correct_flag = False
                    break
            elif type(b[i]) == int and type(a[i]) == list:
                if not compare_lists(a[i],[b[i]]):
                    correct_flag = False
                    break
            elif type(a[i]) == type(b[i]) == int:
                if not compare_lists([a[i]],[b[i]]):
                    correct_flag = False
                    break
            else:
                if not compare_lists(a[i],b[i]):
                    correct_flag = False
                    break


        if correct_flag:
            correct.append(k)

    print("Part 1: ",sum(correct))

if __name__ == "__main__":
    solve()