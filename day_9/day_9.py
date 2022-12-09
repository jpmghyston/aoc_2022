def apply_vector(vector, coord):
    return coord[0] + vector[0], coord[1] + vector[1]


def get_new_tail_coords(head_coords, tail_coords):
    if head_coords == tail_coords:
        # Overlapping, no change
        return tail_coords

    if abs(head_coords[0] - tail_coords[0]) <= 1 and abs(head_coords[1] - tail_coords[1]) <= 1:
        # Touching, no change
        return tail_coords

    if (abs(head_coords[0] - tail_coords[0]) + abs(head_coords[1] - tail_coords[1])) >= 3:
        # Move diagonally
        if head_coords[0] > tail_coords[0]:
            x_vector = 1
        else:
            x_vector = -1
        if head_coords[1] > tail_coords[1]:
            y_vector = 1
        else:
            y_vector = -1
        return apply_vector((x_vector, y_vector), tail_coords)

    if abs(head_coords[0] - tail_coords[0]) > 1:
        if head_coords[0] > tail_coords[0]:
            return apply_vector((1, 0), tail_coords)
        else:
            return apply_vector((-1, 0), tail_coords)

    if abs(head_coords[1] - tail_coords[1]) > 1:
        if head_coords[1] > tail_coords[1]:
            return apply_vector((0, 1), tail_coords)
        else:
            return apply_vector((0, -1), tail_coords)


def get_instructions():
    with open("day9_input.txt") as f:
        return [x.strip().split(" ") for x in f.readlines()]


def get_vector_from_instruction(instruction):
    if instruction == "R":
        vector = (1, 0)
    elif instruction == "U":
        vector = (0, 1)
    elif instruction == "D":
        vector = (0, -1)
    elif instruction == "L":
        vector = (-1, 0)
    else:
        raise "Couldn't parse instruction"
    return vector


def part_1():
    head_coords = (0, 0)
    tail_coords = (0, 0)
    tail_locations_visited = [(0, 0)]
    for instruction, steps in get_instructions():
        vector = get_vector_from_instruction(instruction)
        for _ in range(int(steps)):
            head_coords = apply_vector(vector, head_coords)
            tail_coords = get_new_tail_coords(head_coords, tail_coords)
            tail_locations_visited.append(tail_coords)

    print(len(set(tail_locations_visited)))


def part_2():
    rope = []
    for _ in range(10):
        rope.append((0, 0))
    tail_locations_visited = [(0, 0)]
    for instruction, steps in get_instructions():
        vector = get_vector_from_instruction(instruction)
        for _ in range(int(steps)):
            rope[0] = apply_vector(vector, rope[0])
            for i in range(1, 10):
                rope[i] = get_new_tail_coords(rope[i-1], rope[i])
            tail_locations_visited.append(rope[9])
    print(len(set(tail_locations_visited)))


if __name__ == "__main__":
    part_1()
    part_2()
