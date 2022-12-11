import operator
import math

ops = {"+":operator.add,
       "-":operator.sub,
       "*":operator.mul,
       "/":operator.truediv
}


class Monkey:
    def __init__(self,number):
        self.number = number
        self.lcm = None
        self.items = []
        self.worry_op = None
        self.mod = None
        self.on_true = None
        self.on_false = None
        self.items_inspected = 0

    def increase_worry(self):
        op1, oper, op2 = self.worry_op
        op1_old = op1 == "old"
        op2_old = op2 == "old"
        for i in range(len(self.items)):
            if op1_old:
                op1 = self.items[i]
            else:
                op1 = int(op1)

            if op2_old:
                op2 = self.items[i]
            else:
                op2 = int(op2)

            self.items[i] = ops[oper](op1,op2)

            self.items_inspected += 1

    def decrease_worry(self):
        # Part 1
        # for i in range(len(self.items)):
        #     self.items[i] = operator.floordiv(self.items[i],3)

        # Part 2
        for i in range(len(self.items)):
            self.items[i] %= self.lcm

    def test(self):
        res = []
        for item in self.items:
            if item % self.mod == 0:
                res.append(True)
            else:
                res.append(False)

        return res

    def __str__(self):
        return f"Monkey {self.number}: items inspected {self.items_inspected}"

def run_test(monkeys,round_count):
    for k in range(round_count):
        for i in range(len(monkeys)):
            monkey = monkeys[i]
            monkey.increase_worry()
            monkey.decrease_worry()
            to_move = monkey.test()

            for j in range(len(to_move)):
                item = monkey.items.pop(0)
                if to_move[j]:
                    monkeys[monkey.on_true].items.append(item)
                else:
                    monkeys[monkey.on_false].items.append(item)

        if k in [0,20,1000,2000,3000,4000,5000,6000,7000,8000,9000,10000]:
            print("*********** ROUND", k, "***********")
            for monkey in monkeys:
                print(monkey)

            print()

def solve():
    MONKEY_COUNT = 8
    monkeys = [Monkey(i) for i in range(MONKEY_COUNT)]

    with open("../inputs/day11.txt") as f:
        j = 0
        line = f.readline()
        while line != "":
            line = line.strip()
            # Set monkey
            if line.startswith("Monkey"):
                j = int(line.split(" ")[1][:-1])
            # Load items
            elif line.startswith("Start"):
                items = list(map(int,line.split(":")[1].split(",")))
                monkeys[j].items.extend(items)
            # Set operation
            elif line.startswith("Operation"):
                op1,oper,op2 = line.split(" = ")[1].split(" ")
                monkeys[j].worry_op = (op1,oper,op2)

            # Set test
            elif line.startswith("Test"):
                monkeys[j].mod = int(line.split(" ")[-1])
                monkeys[j].on_true = int(f.readline().strip().split(" ")[-1])
                monkeys[j].on_false = int(f.readline().strip().split(" ")[-1])

            line = f.readline()



    # run_test(monkeys,20)
    # inspection_nums = [monkey.items_inspected for monkey in monkeys]
    # inspection_nums.sort()
    # print("Part 1: ", inspection_nums[-1] * inspection_nums[-2])

    lcm = math.lcm(*[monkey.mod for monkey in monkeys])
    for monkey in monkeys:
        monkey.lcm = lcm

    run_test(monkeys,10000)
    inspection_nums = [monkey.items_inspected for monkey in monkeys]
    inspection_nums.sort()
    print("Part 2: ", inspection_nums[-1] * inspection_nums[-2])



if __name__ == "__main__":
    solve()