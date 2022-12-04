def part_1():
    assignment_pairs = get_assignment_pairs()
    print(len([pair for pair in assignment_pairs if assignment_pair_fully_contained(pair)]))


def part_2():
    assignment_pairs = get_assignment_pairs()
    print(len([pair for pair in assignment_pairs if assignment_pair_overlaps(pair)]))


def get_assignment_pairs():
    with open("day4_input.txt") as f:
        assignment_pairs = [[[int(z) for z in y.split("-")] for y in x.strip().split(",")] for x in f.readlines()]
    return assignment_pairs


def assignment_pair_fully_contained(assignment_pair):
    first_assignment_range, second_assignment_range = get_assignment_ranges(assignment_pair)
    return len(first_assignment_range & second_assignment_range) >= min(len(first_assignment_range), len(second_assignment_range))


def assignment_pair_overlaps(assignment_pair):
    first_assignment_range, second_assignment_range = get_assignment_ranges(assignment_pair)
    return len(first_assignment_range & second_assignment_range) > 0


def get_assignment_ranges(assignment_pair):
    first_assignment, second_assignment = assignment_pair
    first_assignment_range = set(range(first_assignment[0], first_assignment[1] + 1))
    second_assignment_range = set(range(second_assignment[0], second_assignment[1] + 1))
    return first_assignment_range, second_assignment_range


if __name__ == "__main__":
    part_1()
    part_2()
