def get_input():
    # return "mjqjpqmgbljsphdztnvjfqwrcgsmlb"
    with open("day6_input.txt") as f:
        return f.read().strip()


def part_1():
    datastream = get_input()
    for i in range(4, len(datastream)):
        last_four_characters = datastream[i-4:i]
        if not contains_repeated_char(last_four_characters):
            print(i)
            return


def part_2():
    datastream = get_input()
    for i in range(14, len(datastream)):
        last_four_characters = datastream[i-14:i]
        if not contains_repeated_char(last_four_characters):
            print(i)
            return


def contains_repeated_char(string):
    for char in string:
        if string.count(char) > 1:
            return True
    return False


if __name__ == "__main__":
    part_1()
    part_2()
