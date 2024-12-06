def main_a(puzzle_input):
    direction_array = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    visited_positions = set()
    current_direction = 0
    current_position = ()

    layout = [list(line.strip()) for line in puzzle_input]
    for i, row in enumerate(layout):
        if '^' in row:
            current_position = (row.index('^'), i)
            visited_positions.add(current_position)
    
    reached_edge = False
    map_dim = len(layout)
    while not reached_edge:
        x, y = current_position[0] + direction_array[current_direction][0], current_position[1] + direction_array[current_direction][1]
        if x < 0 or y < 0 or x >= map_dim or y >= map_dim:
            reached_edge = True
        elif layout[y][x] == '#':
            current_direction = (current_direction + 1) % 4
        else:
            current_position = (x, y)
            visited_positions.add(current_position)

    return len(visited_positions)


def check_for_loop(layout, starting_position):
    # Dit moet sneller kunnen. Maar is snel genoeg!
    direction_array = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    visited_positions = set()
    visited_positions.add(starting_position)
    current_direction = 0
    current_position = starting_position

    reached_edge = False
    n_steps_retraced = 0
    map_dim = len(layout)

    while not reached_edge:
        x, y = current_position[0] + direction_array[current_direction][0], current_position[1] + direction_array[current_direction][1]
        if x < 0 or y < 0 or x >= map_dim or y >= map_dim:
            reached_edge = True
        elif layout[y][x] == '#':
            current_direction = (current_direction + 1) % 4
            if n_steps_retraced >= 10: # Magisch getalletje: 2 is niet genoeg
                return True
        else:
            current_position = (x, y)
            if current_position in visited_positions:
                n_steps_retraced += 1
            else:
                n_steps_retraced = 0
            visited_positions.add(current_position)

    return False

def main_b(puzzle_input):
    total_working_solutions = 0

    layout = [list(line.strip()) for line in puzzle_input]
    for i, row in enumerate(layout):
        if '^' in row:
            starting_position = (row.index('^'), i)
    
    for y in range(len(layout)):
        for x in range(len(layout)):
            if layout[y][x] == '.':
                layout[y][x] = '#'
                if check_for_loop(layout, starting_position):
                    total_working_solutions += 1
                layout[y][x] = '.'


    return total_working_solutions


if __name__ == '__main__':
    EXAMPLE_MODE = False
    # with open('example.txt', 'r') if EXAMPLE_MODE else open('input.txt', 'r') as full_input:
    #     print(main_a(full_input))
    with open('example.txt', 'r') if EXAMPLE_MODE else open('input.txt', 'r') as full_input:
        print(main_b(full_input))