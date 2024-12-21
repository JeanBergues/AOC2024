def shortest_command(result, pad, exceptions):
    pos = pad['A']
    command_needed = []
    for c in result:
        goal = pad[c]
        if (pos, goal) in exceptions:
            command_needed.extend(exceptions[(pos, goal)])
            command_needed.append('A')
            pos = goal
            continue

        dx, dy = goal[0] - pos[0], goal[1] - pos[1]
        new_step = []
        if dx != 0:
            for _ in range(abs(dx)):
                new_step.append('<' if dx < 0 else '>')
        if dy != 0:
            for _ in range(abs(dy)):
                new_step.append('^' if dy < 0 else 'v')

        if dx > 0 and (pos[0], pos[1] + dy) != (0, 3):
            new_step.reverse()
        command_needed.extend(new_step)
        command_needed.append('A')
        pos = goal

    return command_needed


def dict_key(d, value) -> str:
    for k, v in d.items():
        if v == value:
            return k
    return None


def process_command(command, pad):
    m_dict = {
        '^': (0, -1),
        '<': (-1, 0),
        '>': (1, 0),
        'v': (0, 1)
    }
    pos = pad['A']
    output = ""
    for c in command:
        if c == 'A':
            output += dict_key(pad, pos)
            continue

        pos = (pos[0] + m_dict[c][0], pos[1] + m_dict[c][1])
        if dict_key(pad, pos) == None:
            print("AAAAAAAA HELP DIT MAG HELEMAAL NIET")
            print(pos)
    
    return output


def replay_command(command, numpad, keypad):
    command_to_1 = process_command(command, keypad)
    print(command_to_1)
    command_to_2 = process_command(command_to_1, keypad)
    print(command_to_2)
    output = process_command(command_to_2, numpad)
    print(output)


def main_a(puzzle_input):
    keypad = {
                        '^': (1, 0),    'A': (2, 0),
        '<': (0, 1),    'v': (1, 1),    '>': (2, 1)
    }
    numpad = {
        '7': (0, 0),    '8': (1, 0),    '9': (2, 0),
        '4': (0, 1),    '5': (1, 1),    '6': (2, 1),
        '1': (0, 2),    '2': (1, 2),    '3': (2, 2),
                        '0': (1, 3),    'A': (2, 3)
    }
    keypad_exceptions = {
        ((2,0), (0, 1)): ['v', '<', '<'],
        ((1,0), (0, 1)): ['v', '<'],
    }
    numpad_exceptions = {
        ((1,3), (0, 0)): ['^', '^', '^', '<'],
        ((1,3), (0, 1)): ['^', '^', '<'],
        ((1,3), (0, 2)): ['^', '<'],
        ((2,3), (0, 0)): ['^', '^', '^', '<', '<'],
        ((2,3), (0, 1)): ['^', '^', '<', '<'],
        ((2,3), (0, 2)): ['^', '<', '<'],
    }

    total = 0
    for line in puzzle_input:
        code = list(line.strip())

        numpad_bot_commands = shortest_command(code, numpad, numpad_exceptions)
        bot_2_commands = shortest_command(numpad_bot_commands, keypad, keypad_exceptions)
        bot_1_commands = shortest_command(bot_2_commands, keypad, keypad_exceptions)
        bot_1_commands = shortest_command(bot_1_commands, keypad, keypad_exceptions)
        bot_1_commands = shortest_command(bot_1_commands, keypad, keypad_exceptions)
        bot_1_commands = shortest_command(bot_1_commands, keypad, keypad_exceptions)

        total += len(bot_1_commands) * int("".join(code[:3]))
    
    return total


def n_needed_commands(inp, depth, MAX_DEPTH, mem_dict, res_dict, keypad, keypad_exceptions):
    total = 0
    if depth == MAX_DEPTH:
        return len(inp)
    
    if (inp, depth) in res_dict:
        return res_dict[(inp, depth)]
    
    for ca in inp.split('A'):
        c = ca + 'A'
        if c not in mem_dict:
            mem_dict[c] = "".join(shortest_command(c, keypad, keypad_exceptions))
        # print(c, '\t', mem_dict[c])
        else:
            total += n_needed_commands(mem_dict[c], depth + 1, MAX_DEPTH, mem_dict, res_dict, keypad, keypad_exceptions)

    res_dict[(inp, depth)] = total - 1
    return total - 1


def main_b(puzzle_input):
    keypad = {
                        '^': (1, 0),    'A': (2, 0),
        '<': (0, 1),    'v': (1, 1),    '>': (2, 1)
    }
    numpad = {
        '7': (0, 0),    '8': (1, 0),    '9': (2, 0),
        '4': (0, 1),    '5': (1, 1),    '6': (2, 1),
        '1': (0, 2),    '2': (1, 2),    '3': (2, 2),
                        '0': (1, 3),    'A': (2, 3)
    }
    keypad_exceptions = {
        ((2,0), (0, 1)): ['v', '<', '<'],
        ((0,1), (2,0)): ['>', '>', '^'],
        ((1,0), (0, 1)): ['v', '<'],
        ((0,1), (1, 0)): ['>', '^'],
    }
    numpad_exceptions = {
        ((1,3), (0, 0)): ['^', '^', '^', '<'],
        ((1,3), (0, 1)): ['^', '^', '<'],
        ((1,3), (0, 2)): ['^', '<'],
        ((2,3), (0, 0)): ['^', '^', '^', '<', '<'],
        ((2,3), (0, 1)): ['^', '^', '<', '<'],
        ((2,3), (0, 2)): ['^', '<', '<'],
    }

    total = 0
    total_old = 0
    fastest_routes = {}
    r = 5
    for line in puzzle_input:
        code = list(line.strip())

        bot_commands = shortest_command(code, numpad, numpad_exceptions)
        bot_commands = "".join(bot_commands)
        for _ in range(r):
            new_bot_command = ''
            for ca in bot_commands.split('A'):
                c = ca + 'A'
                if c not in fastest_routes:
                    best_route = "".join(shortest_command(c, keypad, keypad_exceptions))
                    fastest_routes[c] = best_route

                new_bot_command += fastest_routes[c]
            bot_commands = new_bot_command[:-1]

        total_old += len(bot_commands) * int("".join(code[:3]))
        bot_commands = shortest_command(code, numpad, numpad_exceptions)
        bot_commands = "".join(bot_commands)
        total += n_needed_commands(bot_commands, 0, 25, fastest_routes, dict(), keypad, keypad_exceptions) * int("".join(code[:3]))

    # for k, v in fastest_routes.items():
    #     print(k, '\t', v)
    # print(total_old)
    return total


def test_command(puzzle_input):
    keypad = {
                        '^': (1, 0),    'A': (2, 0),
        '<': (0, 1),    'v': (1, 1),    '>': (2, 1)
    }
    numpad = {
        '7': (0, 0),    '8': (1, 0),    '9': (2, 0),
        '4': (0, 1),    '5': (1, 1),    '6': (2, 1),
        '1': (0, 2),    '2': (1, 2),    '3': (2, 2),
                        '0': (1, 3),    'A': (2, 3)
    }
    keypad_exceptions = {
        ((2,0), (0, 1)): ['v', '<', '<'],
        ((1,0), (0, 1)): ['v', '<'],
    }
    numpad_exceptions = {
        ((1,3), (0, 0)): ['^', '^', '^', '<'],
        ((1,3), (0, 1)): ['^', '^', '<'],
        ((1,3), (0, 2)): ['^', '<'],
    }

    command = "v<<A>>^AAAvA^Av<<A>A>^AvA<^A>A<vA<AA>>^AAvAA<^A>Av<<A>A>^AAvA^AA<A>A"
    replay_command(command, numpad, keypad)
    # command = "v<<A>>^A<vA<A>>^AAvAA<^A>Av<<A>>^AAvA^A<vA>^AA<A>Av<<A>A>^AAAvA<^A>A"
    # replay_command(command, numpad, keypad)

    return 0


if __name__ == '__main__':
    EXAMPLE_MODE = False
    file_name = 'example.txt' if EXAMPLE_MODE else 'input.txt'

    with open(file_name, 'r') as full_input:
        # print(main_a(full_input))
        full_input.seek(0)
        print(main_b(full_input))

#   <vA<AA>>^AvAA<^A>A<v<A>>^AvA^A<vA>^A<v<A>^A>AAvA^A<v<A>A>^AAAvA<^A>A
#   v<<A>>^A<A>AvA<^AA>A<vAAA>^A
#   286001109840676
#   294254468894524
