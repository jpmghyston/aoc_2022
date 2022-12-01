def part_1():
    elf_totals = get_elf_totals()
    print("Part 1: {}".format(max(elf_totals)))


def part_2():
    elf_totals = get_elf_totals()
    elf_totals.sort()
    top_three_calories = elf_totals[-3:]
    print("Part 2: {}".format(sum(top_three_calories)))


def get_elf_totals():
    with open("day1_input.txt") as f:
        input = [x.strip() for x in f.readlines()]
    elves = []
    current_elf = []
    for line in input:
        if len(line) == 0:
            elves.append(current_elf)
            current_elf = []
        else:
            current_elf.append(int(line))
    elf_totals = [sum(elf) for elf in elves]
    return elf_totals


if __name__ == "__main__":
    part_1()
    part_2()
