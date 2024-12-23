def main_a(puzzle_input):
    connected_to = {}
    for line in puzzle_input:
        a, b = line.strip().split('-')
        connected_to[a] = connected_to.get(a, set()) | {b}
        connected_to[b] = connected_to.get(b, set()) | {a}

    computer_sets = set()
    visited_computers = set()
    for c1, connections in connected_to.items():
        for c2 in connections - visited_computers:
            for c3 in connected_to[c1] & connected_to[c2]:
                computer_set = tuple(sorted([c1, c2, c3]))
                if any([c.startswith('t') for c in computer_set]):
                    computer_sets.add(computer_set)
        visited_computers.add(c1)
    
    # for s in sorted(list(computer_sets)):
    #     print(s)

    return len(computer_sets)


def find_computer_sets(comps, connections, exclude):
    computer_sets = set()
    possibilities = connections[comps[0]].intersection(*[connections[c] for c in comps]) - exclude
    
    if len(possibilities) == 0:
        exclude.add(comps[-1])
        if len(comps) > 2:
            computer_sets.add(tuple(sorted(comps)))
    else:
        for c in possibilities:
            computer_sets.update(find_computer_sets(comps + [c], connections, exclude))

    return computer_sets


def main_b(puzzle_input):
    connected_to = {}
    for line in puzzle_input:
        a, b = line.strip().split('-')
        connected_to[a] = connected_to.get(a, set()) | {b}
        connected_to[b] = connected_to.get(b, set()) | {a}

    longest_set = ()
    visited_computers = set()

    for c1, _ in connected_to.items():
        computer_sets = find_computer_sets([c1], connected_to, visited_computers.copy())
        for s in computer_sets:
            if len(s) > len(longest_set):
                longest_set = s
        visited_computers.add(c1)

    final_s = ""
    for c in longest_set:
        final_s += c + ','
    return final_s


if __name__ == '__main__':
    EXAMPLE_MODE = False
    file_name = 'example.txt' if EXAMPLE_MODE else 'input.txt'

    with open(file_name, 'r') as full_input:
        print(main_a(full_input))
        full_input.seek(0)
        print(main_b(full_input))