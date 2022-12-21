import re


def get_monkeys():
    with open("day21_input.txt") as f:
        input_lines = [x.strip() for x in f.readlines()]

    operation_monkey_pattern = r"(\w+): (\w+) ([\+-\/\*]) (\w+)"
    number_monkey_pattern = r"(\w+): (\d+)"

    number_monkeys = {}
    operation_monkeys = {}

    for line in input_lines:
        if re.match(operation_monkey_pattern, line):
            result = re.search(operation_monkey_pattern, line)
            operation_monkeys[result.group(1)] = {"op": result.group(3), 1: result.group(2), 2: result.group(4)}
        elif re.match(number_monkey_pattern, line):
            result = re.search(number_monkey_pattern, line)
            number_monkeys[result.group(1)] = int(result.group(2))
    return number_monkeys, operation_monkeys


def part_1():
    number_monkeys, operation_monkeys = get_monkeys()
    while len(operation_monkeys.keys()) > 0:
        for key, val in operation_monkeys.items():
            if len({val[1], val[2]}.intersection(set(number_monkeys.keys()))) == 2:
                process_monkey(key, number_monkeys, operation_monkeys, val)
    print(number_monkeys["root"])


def part_2():
    number_monkeys, operation_monkeys = get_monkeys()
    first, second = test_monkeys(number_monkeys, operation_monkeys)
    i = second - first
    while True:
        number_monkeys, operation_monkeys = get_monkeys()
        number_monkeys["humn"] = i
        first, second = test_monkeys(number_monkeys, operation_monkeys)
        if first == second:
            break
        else:
            i -= (second - first) / 120


def test_monkeys(number_monkeys, operation_monkeys):
    while len(operation_monkeys.keys()) > 0:
        for key, val in operation_monkeys.items():
            if len({val[1], val[2]}.intersection(set(number_monkeys.keys()))) == 2:
                if key == "root":
                    return number_monkeys[val[1]], number_monkeys[val[2]]
                process_monkey(key, number_monkeys, operation_monkeys, val)


def process_monkey(key, number_monkeys, operation_monkeys, val):
    if val["op"] == "+":
        number_monkeys[key] = number_monkeys[val[1]] + number_monkeys[val[2]]
    elif val["op"] == "-":
        number_monkeys[key] = number_monkeys[val[1]] - number_monkeys[val[2]]
    elif val["op"] == "*":
        number_monkeys[key] = number_monkeys[val[1]] * number_monkeys[val[2]]
    elif val["op"] == "/":
        number_monkeys[key] = number_monkeys[val[1]] / number_monkeys[val[2]]
    else:
        raise "Error, should never get here"
    operation_monkeys.pop(key)


if __name__ == "__main__":
    part_1()
    part_2()
