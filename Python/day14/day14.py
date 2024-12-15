import numpy as np

def main_a(puzzle_input, xlim, ylim):
    safety_score = 1
    quadrant_robots = [0, 0, 0, 0]
    simulate_seconds = 100

    for line in puzzle_input:
        x, y = [*map(int, line.split(' ')[0][2:].split(','))]
        vx, vy = [*map(int, line.split(' ')[1][2:].split(','))]
        for _ in range(simulate_seconds):
            x = (x + vx) % xlim
            y = (y + vy) % ylim
        
        quadrant = -1
        if x < xlim // 2:
            if y < ylim // 2:
                quadrant = 0
            elif y > ylim // 2:
                quadrant = 1
        elif x > xlim // 2:
            if y < ylim // 2:
                quadrant = 2
            elif y > ylim // 2:
                quadrant = 3

        if quadrant >= 0:
            quadrant_robots[quadrant] += 1
            
    for robots in quadrant_robots:
        safety_score *= robots

    return safety_score


def fancy_print(grid):
    final_string = ""
    for line in grid:
        for val in line:
            final_string += '@' if val else '_'
        final_string += '\n'
    print(final_string)


def main_b(puzzle_input, xlim, ylim):
    robots = []

    for line in puzzle_input:
        x, y = [*map(int, line.split(' ')[0][2:].split(','))]
        vx, vy = [*map(int, line.split(' ')[1][2:].split(','))]
        robots.append((x, y, vx, vy))

    second = 1
    while True:
        new_grid = np.full((ylim, xlim), False)
        new_positions = set()
        for i, (x, y, vx, vy) in enumerate(robots):
            new_x = (x + vx) % xlim
            new_y = (y + vy) % ylim
            new_grid[new_y, new_x] = True
            robots[i] = (new_x, new_y, vx, vy)
            new_positions.add((new_x, new_y))

        total_double_neighbours = 0
        for x, y in new_positions:
            total_neighbours = 0
            for d in [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]:
                if (x + d[0], y + d[1]) in new_positions:
                    total_neighbours += 1
            if total_neighbours >= 8:
                total_double_neighbours += 1

        if total_double_neighbours >= 10:
            return second
        else:
            second += 1


if __name__ == '__main__':
    EXAMPLE_MODE = False
    limits = (11, 7) if EXAMPLE_MODE else (101, 103)
    # with open('example.txt', 'r') if EXAMPLE_MODE else open('input.txt', 'r') as full_input:
    #     print(main_a(full_input, *limits))
    with open('example.txt', 'r') if EXAMPLE_MODE else open('input.txt', 'r') as full_input:
        print(main_b(full_input, *limits))