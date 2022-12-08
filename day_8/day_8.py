with open("day8_input.txt") as f:
    grid = [[int(y) for y in x.strip()] for x in f.readlines()]

height = len(grid)
width = len(grid[0])

visible_count = (height*2 + width*2) - 4
non_visible_count = 0
total = height * width

max_scenic_score = 0


def max_tree_height(tree_list):
    if len(tree_list) == 0:
        return 0
    return max(tree_list)


def trees_visible(tree_height_considered, tree_list):
    trees_visible_in_direction = 0
    for tree in tree_list:
        trees_visible_in_direction += 1
        if tree >= tree_height_considered:
            break
    return trees_visible_in_direction


for i in range(1, height - 1):
    for j in range(1, width - 1):
        tree_height = grid[i][j]
        trees_left = grid[i][:j]
        trees_right = grid[i][j+1:]
        trees_up = [grid[x][j] for x in range(0, i)]
        trees_down = [grid[x][j] for x in range(i + 1, height)]

        # Part 1
        max_tree_height_each_direction = [
            max_tree_height(trees_up),
            max_tree_height(trees_down),
            max_tree_height(trees_right),
            max_tree_height(trees_left)
        ]
        if tree_height > min(max_tree_height_each_direction):
            visible_count += 1
        else:
            non_visible_count += 1

        # Part 2
        tree_score = trees_visible(tree_height, reversed(trees_left)) * trees_visible(tree_height, trees_right) * trees_visible(tree_height, reversed(trees_up)) * trees_visible(tree_height, trees_down)
        if max_scenic_score < tree_score:
            max_scenic_score = tree_score

print(visible_count)
print(max_scenic_score)


