def step(x, y, plant, garden, bound, visited_fields):
    area = 1
    perimeter = 0
    visited_fields.add((x, y))

    for d in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        test_x, test_y = x + d[0], y + d[1]
        if (test_x, test_y) not in visited_fields:
            if 0 <= test_x < bound and 0 <= test_y < bound and garden[test_x][test_y] == plant:
                extra_area, extra_perimeter = step(test_x, test_y, plant, garden, bound, visited_fields)
                area += extra_area
                perimeter += extra_perimeter
            else:
                perimeter += 1

    return (area, perimeter)


def count_sides(fields):
    total_sides = 0

    for field in fields:
        for d1, d2 in [((1, 0), (0, 1)), ((1, 0), (0, -1)), ((-1, 0), (0, 1)), ((-1, 0), (0, -1))]:
            if (field[0] + d1[0], field[1] + d1[1]) not in fields and (field[0] + d2[0], field[1] + d2[1]) not in fields:
                total_sides += 1
            if (field[0] + d1[0], field[1] + d1[1]) in fields and (field[0] + d2[0], field[1] + d2[1]) in fields and (field[0] + d1[0] + d2[0], field[1]+ d1[1] + d2[1]) not in fields:
                total_sides += 1

    return total_sides


def main_a(puzzle_input):
    garden = list(map(list, puzzle_input.read().split('\n')))
    BOUND = len(garden)
    total_price = 0
    
    for x in range(BOUND):
        for y in range(BOUND):
            if garden[x][y] != '-':
                visited_fields = set()
                area, perimeter = step(x, y, garden[x][y], garden, BOUND, visited_fields)
                total_price += area * perimeter
                for c in visited_fields:
                    garden[c[0]][c[1]] = '-'
            
    return total_price


def main_b(puzzle_input):
    garden = list(map(list, puzzle_input.read().split('\n')))
    BOUND = len(garden)
    total_price = 0
    
    for x in range(BOUND):
        for y in range(BOUND):
            if garden[x][y] != '-':
                visited_fields = set()
                area, _ = step(x, y, garden[x][y], garden, BOUND, visited_fields)
                total_sides = count_sides(visited_fields)
                total_price += area * total_sides

                for c in visited_fields:
                    garden[c[0]][c[1]] = '-'
            
    return total_price


if __name__ == '__main__':
    EXAMPLE_MODE = False
    with open('example.txt', 'r') if EXAMPLE_MODE else open('input.txt', 'r') as full_input:
        print(main_a(full_input))
    with open('example.txt', 'r') if EXAMPLE_MODE else open('input.txt', 'r') as full_input:
        print(main_b(full_input))