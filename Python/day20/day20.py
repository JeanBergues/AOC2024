def dijkstra(maze, source, goal, BOUND):
    directions = [(1, 0), (0, -1), (0, 1), (-1, 0)]
    visited = set()
    visited.add(source)

    solution = {}
    queue = []
    solution[source] = 0
    queue.append((0, source))

    while queue:
        queue.sort(key=lambda x: -1*x[0]) # Sort queue on path length smallest first
        length, coordinates = queue.pop()

        if coordinates == goal:
            return solution
        
        for d in directions:
            nx, ny = coordinates[0] + d[0], coordinates[1] + d[1]

            if 0 <= nx < BOUND and 0 <= ny < BOUND and maze[ny][nx] != '#' and (nx, ny) not in visited:
                visited.add((nx, ny))
                solution[(nx, ny)] = length + 1
                queue.append((length + 1, (nx, ny)))

    return None


def dist(start, end):
    return abs(start[0] - end[0]) + abs(start[1] + end[1])


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

    BOUND = len(maze)

    path_lengths = dijkstra(maze, start, goal, BOUND)
    default_path_length = path_lengths[goal]
    
    shortcuts = []
    for y in range(1, BOUND - 1):
        for x in range(1, BOUND - 1):
            if maze[y][x] == '.':
                # Check horizontal shortcuts
                if x != BOUND - 2:
                    if maze[y][x+1] == '#' and maze[y][x+2] == '.':
                        shortcuts.append(((x, y), (x+2, y)))
                # Check vertical shortcuts
                if y != BOUND - 2:
                    if maze[y+1][x] == '#' and maze[y+2][x] == '.':
                        shortcuts.append(((x, y), (x, y+2)))

    check = {}
    at_least_100 = 0

    for shortcut in shortcuts:
        saved_steps = abs(path_lengths[shortcut[0]] - path_lengths[shortcut[1]]) - 2
        check[saved_steps] = check.get(saved_steps, 0) + 1
        if saved_steps >= 100: at_least_100 += 1

    # for k, v in sorted(check.items()): print(k, '\t', v)

    return at_least_100


def main_b(puzzle_input):
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

    BOUND = len(maze)
    min_save = 100
    max_cheat_length = 20

    path_lengths = dijkstra(maze, start, goal, BOUND)
    full_path_length = path_lengths[goal]
    check = {}
    min_100_cheats = 0

    for cheat_start, length_to_start in path_lengths.items():
        if full_path_length - length_to_start < min_save:
            continue

        for cl in range(2, max_cheat_length + 1):
            for dy in range(-cl, cl + 1):
                x1, x2 = -(cl - abs(dy)), cl - abs(dy)
                test1, test2 = (cheat_start[0] + x1, cheat_start[1] + dy), (cheat_start[0] + x2, cheat_start[1] + dy)
                if test1 in path_lengths:
                    saved = path_lengths[test1] - path_lengths[cheat_start] - cl
                    if saved >= min_save: 
                        check[saved] = check.get(saved, 0) + 1
                        min_100_cheats += 1
                if x1 != x2 and test2 in path_lengths:
                    saved = path_lengths[test2] - path_lengths[cheat_start] - cl
                    if saved >= min_save: 
                        check[saved] = check.get(saved, 0) + 1
                        min_100_cheats += 1

    for k, v in sorted(check.items()): print(k, '\t', v)

    return min_100_cheats


if __name__ == '__main__':
    EXAMPLE_MODE = False
    file_name = 'example.txt' if EXAMPLE_MODE else 'input.txt'

    with open(file_name, 'r') as full_input:
        print(main_a(full_input))
        full_input.seek(0)
        print(main_b(full_input))