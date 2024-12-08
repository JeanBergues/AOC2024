def main_a(puzzle_input):
    unique_antinodes = set()
    coordinate_dict = {}
    BOUND = 0

    for y, row in enumerate(puzzle_input):
        for x, c in enumerate(list(row.strip())):
            BOUND = len(row)
            if c != '.':
                if c not in coordinate_dict:
                    coordinate_dict[c] = [(x, y)]
                else:
                    coordinate_dict[c].append((x, y))

    for antennas in coordinate_dict.values():
        for i in range(len(antennas)):
            for j in range(i+1, len(antennas)):
                a1, a2 = antennas[i], antennas[j]
                difference = (a2[0] - a1[0], a2[1] - a1[1])
                an1 = (a1[0] - difference[0], a1[1] - difference[1])
                an2 = (a2[0] + difference[0], a2[1] + difference[1])
                
                if 0 <= an1[0] < BOUND and 0 <= an1[1] < BOUND:
                    unique_antinodes.add(an1)
                if 0 <= an2[0] < BOUND and 0 <= an2[1] < BOUND:
                    unique_antinodes.add(an2)

    return len(unique_antinodes)


def main_b(puzzle_input):
    unique_antinodes = set()
    coordinate_dict = {}
    BOUND = 0

    for y, row in enumerate(puzzle_input):
        for x, c in enumerate(list(row.strip())):
            BOUND = len(row)
            if c != '.':
                if c not in coordinate_dict:
                    coordinate_dict[c] = [(x, y)]
                else:
                    coordinate_dict[c].append((x, y))

    for antennas in coordinate_dict.values():
        for i in range(len(antennas)):
            for j in range(i+1, len(antennas)):
                a1, a2 = antennas[i], antennas[j]
                difference = (a2[0] - a1[0], a2[1] - a1[1])

                out_of_bounds = False
                k = 0
                while not out_of_bounds:
                    an = (a1[0] - k*difference[0], a1[1] - k*difference[1])
                    if 0 <= an[0] < BOUND and 0 <= an[1] < BOUND:
                        unique_antinodes.add(an)
                        k += 1
                    else:
                        out_of_bounds = True

                out_of_bounds = False
                k = 1
                while not out_of_bounds:
                    an = (a1[0] + k*difference[0], a1[1] + k*difference[1])
                    if 0 <= an[0] < BOUND and 0 <= an[1] < BOUND:
                        unique_antinodes.add(an)
                        k += 1
                    else:
                        out_of_bounds = True

    return len(unique_antinodes)


if __name__ == '__main__':
    EXAMPLE_MODE = False
    # with open('example.txt', 'r') if EXAMPLE_MODE else open('input.txt', 'r') as full_input:
    #     print(main_a(full_input))
    with open('example.txt', 'r') if EXAMPLE_MODE else open('input.txt', 'r') as full_input:
        print(main_b(full_input))