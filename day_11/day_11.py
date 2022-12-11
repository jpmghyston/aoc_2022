from math import lcm


class Monkey:
    def __init__(self, items, operation, test_divide_by, monkey_if_true, monkey_if_false):
        self.items = items
        self.operation = operation
        self.monkey_if_true = monkey_if_true
        self.monkey_if_false = monkey_if_false
        self.inspection_count = 0
        self.test_divide_by = test_divide_by
        self.test = lambda x: x % test_divide_by == 0

    def receive_item(self, item):
        self.items.append(item)

    def process_items(self, monkey_list, least_common_multiple=None):
        for item in self.items:
            item = self.operation(item)
            if least_common_multiple:
                item = item % least_common_multiple
            else:
                item = item // 3
            if self.test(item):
                monkey_list[self.monkey_if_true].receive_item(item)
            else:
                monkey_list[self.monkey_if_false].receive_item(item)
            self.inspection_count += 1
        self.items = []


test_monkeys = [
    Monkey(
        items = [79, 98],
        operation = lambda x: x * 19,
        test_divide_by = 23,
        monkey_if_true = 2,
        monkey_if_false = 3
    ),
    Monkey(
        items = [54, 65, 75, 74],
        operation = lambda x: x + 6,
        test_divide_by = 19,
        monkey_if_true = 2,
        monkey_if_false = 0
    ),
    Monkey(
        items = [79, 60, 97],
        operation = lambda x: x * x,
        test_divide_by = 13,
        monkey_if_true = 1,
        monkey_if_false = 3
    ),
    Monkey(
        items = [74],
        operation = lambda x: x + 3,
        test_divide_by = 17,
        monkey_if_true = 0,
        monkey_if_false = 1
    )   
]

real_monkeys = [
    # 0
    Monkey(
        items = [97, 81, 57, 57, 91, 61],
        operation = lambda x: x * 7,
        test_divide_by =  11,
        monkey_if_true = 5,
        monkey_if_false = 6
    ),
    # 1
    Monkey(
        items = [88, 62, 68, 90],
        operation = lambda x: x * 17,
        test_divide_by = 19,
        monkey_if_true = 4,
        monkey_if_false = 2
    ),
    # 2
    Monkey(
        items = [74, 87],
        operation = lambda x: x + 2,
        test_divide_by = 5,
        monkey_if_true = 7,
        monkey_if_false = 4
    ),
    # 3
    Monkey(
        items = [53, 81, 60, 87, 90, 99, 75],
        operation = lambda x: x + 1,
        test_divide_by = 2,
        monkey_if_true = 2,
        monkey_if_false = 1
    ),   
    # 4
    Monkey(
        items = [57],
        operation = lambda x: x + 6,
        test_divide_by = 13,
        monkey_if_true = 7,
        monkey_if_false = 0
    ),  
    # 5
    Monkey(
        items = [54, 84, 91, 55, 59, 72, 75, 70],
        operation = lambda x: x * x,
        test_divide_by = 7,
        monkey_if_true = 6,
        monkey_if_false = 3
    ),
    # 6
    Monkey(
        items = [95, 79, 79, 68, 78],
        operation = lambda x: x + 3,
        test_divide_by = 3,
        monkey_if_true = 1,
        monkey_if_false = 3
    ),
    # 7
    Monkey(
        items = [61, 97, 67],
        operation = lambda x: x + 4,
        test_divide_by = 17,
        monkey_if_true = 0,
        monkey_if_false = 5
    ),
]

print_rounds = [0, 19, 1000 - 1, 2000 - 1, 3000 - 1]

def part_1(monkey_list):
    for i in range(20):
        for monkey in monkey_list:
            monkey.process_items(monkey_list)
    monkey_counts = sorted([monkey.inspection_count for monkey in monkey_list])
    monkey_business = monkey_counts[-1] * monkey_counts[-2]
    print(monkey_business)

def part_2(monkey_list):
    least_common_multiple = lcm(*[monkey.test_divide_by for monkey in monkey_list])
    for i in range(10000):
        for monkey in monkey_list:
            monkey.process_items(monkey_list, least_common_multiple)

        # if i in print_rounds:
        #     print("After round {}".format(i + 1))
        #     for i, monkey in enumerate(monkey_list):
        #         print("Monkey {} inspected items {} times".format(i, monkey.inspection_count))
    monkey_counts = sorted([monkey.inspection_count for monkey in monkey_list])
    monkey_business = monkey_counts[-1] * monkey_counts[-2]
    print(monkey_business)

part_1(test_monkeys)
part_2(test_monkeys)