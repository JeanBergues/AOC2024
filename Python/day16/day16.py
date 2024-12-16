PART_A_SHORTEST_LENGTH = 1e9
shortest_path_to_dict = {}
best_paths = []

def shortest_path_from(x, y, facing, current_length, visited, maze, goal):
    global PART_A_SHORTEST_LENGTH
    global shortest_path_to_dict
    global best_paths

    if len(visited) > 500:
        return

    if current_length <= shortest_path_to_dict.get((x, y, facing), 1e9):
        shortest_path_to_dict[(x, y, facing)] = current_length
    else:
        return

    if (x, y) == goal:
        if current_length <= PART_A_SHORTEST_LENGTH:
            PART_A_SHORTEST_LENGTH = current_length
            best_paths.append((current_length, visited))
        return
    if current_length > PART_A_SHORTEST_LENGTH:
        return

    directions = [(1, 0), (0, -1), (0, 1), (-1, 0)]
    directions.remove((-1 * facing[0], -1 * facing[1]))

    for d in directions:
        new_x, new_y = x + d[0], y + d[1]
        if maze[new_y][new_x] == '.' and (new_x, new_y) not in visited:
            movement_cost = 1 if d == facing else 1001
            new_visited = visited.copy() | set([(x, y)])
            shortest_path_from(new_x, new_y, d, current_length + movement_cost, new_visited, maze, goal)

    return


def main_a(puzzle_input):
    maze = []
    for y, line in enumerate(puzzle_input):
        new_maze_row = list(line.strip())
        if 'E' in new_maze_row:
            goal = (new_maze_row.index('E'), y)
            new_maze_row[new_maze_row.index('E')] = '.'
        if 'S' in new_maze_row:
            start = (new_maze_row.index('S'), y)
            new_maze_row[new_maze_row.index('S')] = '.'
        maze.append(new_maze_row)

    shortest_path_from(*start, (1, 0), 0, set(), maze, goal)

    return PART_A_SHORTEST_LENGTH


def main_b(puzzle_input):
    global best_paths

    maze = []
    for y, line in enumerate(puzzle_input):
        new_maze_row = list(line.strip())
        if 'E' in new_maze_row:
            goal = (new_maze_row.index('E'), y)
            new_maze_row[new_maze_row.index('E')] = '.'
        if 'S' in new_maze_row:
            start = (new_maze_row.index('S'), y)
            new_maze_row[new_maze_row.index('S')] = '.'
        maze.append(new_maze_row)

    shortest_path_from(*start, (1, 0), 0, set(), maze, goal)

    tiles_in_best_paths = set()
    for paths in best_paths:
        if paths[0] == PART_A_SHORTEST_LENGTH:
            tiles_in_best_paths |= paths[1]

    return len(tiles_in_best_paths) + 1


if __name__ == '__main__':
    EXAMPLE_MODE = False
    # with open('example.txt', 'r') if EXAMPLE_MODE else open('input.txt', 'r') as full_input:
    #     print(main_a(full_input))
    with open('example.txt', 'r') if EXAMPLE_MODE else open('input.txt', 'r') as full_input:
        print(main_b(full_input))