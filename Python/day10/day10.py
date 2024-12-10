def paths_set_from_pos(x, y, tm, bound):
    reachable_nines = set()
    current_level = tm[x][y]

    if current_level == 9:
        reachable_nines.add((x, y))
        return reachable_nines

    for d in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        test_x, test_y = x + d[0], y + d[1]
        if 0 <= test_x < bound and 0 <= test_y < bound:
            new_level = tm[test_x][test_y]
            if new_level - current_level == 1:
                reachable_nines = reachable_nines | paths_set_from_pos(test_x, test_y, tm, bound)

    return reachable_nines


def paths_from_pos(x, y, tm, bound):
    reachable_nines = 0
    current_level = tm[x][y]

    if current_level == 9:
        return 1

    for d in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        test_x, test_y = x + d[0], y + d[1]
        if 0 <= test_x < bound and 0 <= test_y < bound:
            new_level = tm[test_x][test_y]
            if new_level - current_level == 1:
                reachable_nines += paths_from_pos(test_x, test_y, tm, bound)

    return reachable_nines


def main_a(puzzle_input):
    total_trailhead_score = 0
    topographic_map = []

    for line in puzzle_input:
        topographic_map.append([int(c) for c in line.strip()])
    
    bound = len(topographic_map[0])

    for x in range(bound):
        for y in range(bound):
            if topographic_map[x][y] == 0:
                n = paths_set_from_pos(x, y, topographic_map, bound)
                total_trailhead_score += len(n)

    return total_trailhead_score


def main_b(puzzle_input):
    total_trailhead_score = 0
    topographic_map = []

    for line in puzzle_input:
        topographic_map.append([int(c) for c in line.strip()])
    
    bound = len(topographic_map[0])

    for x in range(bound):
        for y in range(bound):
            if topographic_map[x][y] == 0:
                n = paths_from_pos(x, y, topographic_map, bound)
                total_trailhead_score += n

    return total_trailhead_score


if __name__ == '__main__':
    EXAMPLE_MODE = False
    with open('example.txt', 'r') if EXAMPLE_MODE else open('input.txt', 'r') as full_input:
        print(main_a(full_input))
    with open('example.txt', 'r') if EXAMPLE_MODE else open('input.txt', 'r') as full_input:
        print(main_b(full_input))

# for y in range(bound):
#         for x in range(bound):
#             current_level = topographic_map[y][x]
#             if current_level == 0 or current_level == 9:
#                 continue

#             l_levels, h_levels = 0, 0
#             for d in directions:
#                 test_x, test_y = x + d[0], y + d[1]
#                 if 0 <= test_x < bound and 0 <= test_y < bound:
#                     new_level = topographic_map[test_y][test_x]
#                     if current_level - new_level == 1:
#                         l_levels += 1
#                     if current_level - new_level == -1:
#                         h_levels += 1
                
#             if l_levels == 0 or h_levels == 0:
#                 topographic_map[y][x] = 100