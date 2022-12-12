with open("day12_input.txt") as f:
    grid = [[char for char in line.strip()] for line in f.readlines()]


def get_coords_of_letter(grid, letter):
    for a in range(len(grid)):
        for b in range(len(grid[0])):
            if grid[a][b] == letter:
                yield a, b


def get_height_of_letter(letter):
    if letter == "S":
        return ord("a")
    elif letter == "E":
        return ord("z")
    else:
        return ord(letter)


coords_of_start = next(get_coords_of_letter(grid, "S"))
coords_of_end = next(get_coords_of_letter(grid, "E"))


def get_grid_graph():
    graph = {}
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            current_coords = (i, j)
            connecting_coords = set()
            grid_letter = grid[i][j]
            max_height_to_go_to = get_height_of_letter(grid[i][j]) + 1
            if i - 1 >= 0 and get_height_of_letter(grid[i - 1][j]) <= max_height_to_go_to:
                connecting_coords.add((i - 1, j))
            if i + 1 < len(grid) and get_height_of_letter(grid[i + 1][j]) <= max_height_to_go_to:
                connecting_coords.add((i + 1, j))
            if j - 1 >= 0 and get_height_of_letter(grid[i][j - 1]) <= max_height_to_go_to:
                connecting_coords.add((i, j - 1))
            if j + 1 < len(grid[0]) and get_height_of_letter(grid[i][j + 1]) <= max_height_to_go_to:
                connecting_coords.add((i, j + 1))
            graph[current_coords] = connecting_coords
    return graph


graph = get_grid_graph()


def shortest_path(graph, node1, node2):
    path_list = [[node1]]
    path_index = 0
    # To keep track of previously visited nodes
    previous_nodes = {node1}
    if node1 == node2:
        return path_list[0]

    while path_index < len(path_list):
        current_path = path_list[path_index]
        last_node = current_path[-1]
        next_nodes = graph[last_node]
        # Search goal node
        if node2 in next_nodes:
            current_path.append(node2)
            return current_path
        # Add new paths
        for next_node in next_nodes:
            if next_node not in previous_nodes:
                new_path = current_path[:]
                new_path.append(next_node)
                path_list.append(new_path)
                # To avoid backtracking
                previous_nodes.add(next_node)
        # Continue to next path in list
        path_index += 1
    # No path is found
    return []


# Part 1
print(len(shortest_path(graph, coords_of_start, coords_of_end)) - 1)

# Part 2
coords = [coord for coord in get_coords_of_letter(grid, "a")]
coords.append(next(get_coords_of_letter(grid, "S")))
print(coords)
shortest_path_length = None
for i, coord in enumerate(coords):
    path_length = len(shortest_path(graph, coord, coords_of_end)) - 1
    if shortest_path_length is None:
        shortest_path_length = path_length
    if path_length > 0 and path_length < shortest_path_length:
        shortest_path_length = path_length

print(shortest_path_length)
