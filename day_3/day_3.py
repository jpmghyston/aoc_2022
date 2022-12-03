def part_1():
    input_vals = get_input()
    backpacks = [[x[0:(len(x)//2)], x[len(x)//2:]] for x in input_vals]
    print(sum([get_priority_of_item(get_duplicated_item(backpack)) for backpack in backpacks]))

def part_2():
    backpacks = get_input()
    groups = [[]]
    group_index = 0
    for i, backpack in enumerate(backpacks):
        if i > 0 and i % 3 == 0:
            group_index += 1
            groups.append([])
        groups[group_index].append(set([x for x in backpack]))
    print(sum([get_priority_for_group(group) for group in groups]))
    
def get_priority_for_group(group):
    badges = group[0] & group[1] & group[2]
    if len(badges) > 1:
        raise "Shouldn't happen!"
    for badge in badges:
        return get_priority_of_item(badge)
    

def get_input():
    with open('day3_input.txt') as f:
        input_vals = [x.strip() for x in f.readlines()]
    return input_vals

def get_duplicated_item(backpack):
    for item in backpack[0]:
        for other_item in backpack[1]:
            if item == other_item:
                return item

def get_priority_of_item(item):
    if item.isupper():
        return ord(item) - 38
    return ord(item) - 96

if __name__ == "__main__":
    part_1()
    part_2()
