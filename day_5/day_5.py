from copy import deepcopy

test_crates = [
    ["Z", "N"],
    ["M", "C", "D"],
    ["P"]
]

real_crates = [
    ["D", "L", "J", "R", "V", "G", "F"],
    ["T", "P", "M", "B", "V", "H", "J", "S"],
    ["V", "H", "M", "F", "D", "G", "P", "C"],
    ["M", "D", "P", "N", "G", "Q"],
    ["J", "L", "H", "N", "F"],
    ["N", "F", "V", "Q", "D", "G", "T", "Z"],
    ["F", "D", "B", "L"],
    ["M", "J", "B", "S", "V", "D", "N"],
    ["G", "L", "D"]
]


def part_1():
    move_instructions = get_move_instructions()
    # crates = deepcopy(test_crates)
    crates = deepcopy(real_crates)
    for instruction in move_instructions:
        for _ in range(instruction[0]):
            crate_to_move = crates[instruction[1] - 1].pop()
            crates[instruction[2] - 1].append(crate_to_move)
    print_crate_message(crates)


def part_2():
    move_instructions = get_move_instructions()
    # crates = deepcopy(test_crates)
    crates = deepcopy(real_crates)
    for instruction in move_instructions:
        crates_to_move = crates[instruction[1] - 1][instruction[0]*-1:]
        remaining_crates = crates[instruction[1] - 1][:(instruction[0]*-1)]
        crates[instruction[1] - 1] = remaining_crates
        crates[instruction[2] - 1] += crates_to_move
    print_crate_message(crates)


def print_crate_message(crates):
    message = "".join([x.pop() for x in crates])
    print(message)


def get_move_instructions():
    with open("day5_input.txt") as f:
        move_instructions = [[int(y) for y in x.strip().split(" ") if y.isdigit()] for x in f.readlines()]
    return move_instructions


if __name__ == "__main__":
    part_1()
    part_2()
