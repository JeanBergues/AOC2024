def read_in_keys_locks(puzzle_input):
    keys, locks = [], []
    for scheme in puzzle_input.read().split('\n\n'):
        new_scheme = [0]*5
        scheme_array = scheme.splitlines()

        for i in range(len(scheme_array[0])):
            new_scheme[i] = [row[i] for row in scheme_array].count('#') - 1

        if scheme[0] == '#':
            locks.append(tuple(new_scheme))
        else:
            keys.append(tuple(new_scheme))

    return (keys, locks)


def check_key_lock_combo(key, lock):
    for k, l in zip(key, lock):
        if l + k > 5:
            return False
    return True


def main_a(puzzle_input):
    keys, locks = read_in_keys_locks(puzzle_input)

    total_pairs = 0
    for key in keys:
        for lock in locks:
            if check_key_lock_combo(key, lock):
                total_pairs += 1

    return total_pairs


if __name__ == '__main__':
    EXAMPLE_MODE = False
    file_name = 'example.txt' if EXAMPLE_MODE else 'input.txt'

    with open(file_name, 'r') as full_input:
        print(main_a(full_input))