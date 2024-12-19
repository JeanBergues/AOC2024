def dijkstra(walls, source, goal, BOUND):
    directions = [(1, 0), (0, -1), (0, 1), (-1, 0)]
    visited = set()
    visited.add(source)

    solution = []
    queue = []
    solution.append((0, source))
    queue.append((0, source))

    while queue:
        queue.sort(key=lambda x: -1*x[0]) # Sort queue on path length smallest first
        length, coordinates = queue.pop()

        if coordinates == goal:
            return length
        
        for d in directions:
            nx, ny = coordinates[0] + d[0], coordinates[1] + d[1]

            if 0 <= nx < BOUND and 0 <= ny < BOUND and (nx, ny) not in walls and (nx, ny) not in visited:
                visited.add((nx, ny))
                solution.append((length + 1, (nx, ny)))
                queue.append((length + 1, (nx, ny)))

    return None


def main_a(puzzle_input, BOUND):
    walls = set()
    n_bytes = 12 if BOUND == 7 else 1024
    for i, line in enumerate(puzzle_input):
        a, b = map(int, line.split(','))
        walls.add((a, b))
        if i == n_bytes-1: break

    goal = (BOUND-1, BOUND-1)
    shortest_path = dijkstra(walls, (0, 0), goal, BOUND)

    return shortest_path


def main_b(puzzle_input, BOUND):
    walls = set()
    goal = (BOUND-1, BOUND-1)

    for i, line in enumerate(puzzle_input):
        a, b = map(int, line.split(','))
        walls.add((a, b))
        if i <= 1024: continue

        shortest_path = dijkstra(walls, (0, 0), goal, BOUND)
        if shortest_path == None:
            return (a, b)


if __name__ == '__main__':
    EXAMPLE_MODE = False
    file_name = 'example.txt' if EXAMPLE_MODE else 'input.txt'
    maze_bound = 7 if EXAMPLE_MODE else 71

    with open(file_name, 'r') as full_input:
        print(main_a(full_input, maze_bound))
        full_input.seek(0)
        print(main_b(full_input, maze_bound))