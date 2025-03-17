import numpy as np
from timeit import timeit

# 10000x = 9.697508600074798
def main_a(puzzle_input):
    left_list, right_list = [], []
    for line in puzzle_input:
        a, b = line.split()
        left_list.append(int(a))
        right_list.append(int(b))

    left_list.sort()
    right_list.sort()

    total = 0
    for i in range(len(left_list)):
        total += abs(left_list[i] - right_list[i])

    return total

# 10000x = 9.449204899836332
def main_a_np(puzzle_input):
    left_list, right_list = [], []
    for line in puzzle_input:
        a, b = line.split()
        left_list.append(int(a))
        right_list.append(int(b))

    left_list.sort()
    right_list.sort()
    return np.sum(np.abs(np.array(left_list) - np.array(right_list)))


# 10000x = 10.081642600009218
def main_a_np_preallocate(puzzle_input):
    n_lines = 0
    for line in puzzle_input:
        n_lines += 1
    puzzle_input.seek(0)

    left_list, right_list = np.zeros(n_lines), np.zeros(n_lines)
    for i, line in enumerate(puzzle_input):
        a, b = line.split()
        left_list[i] = int(a)
        right_list[i] = int(b)

    left_list.sort()
    right_list.sort()
    return np.sum(np.abs(left_list - right_list))


# 10000x = 8.586051600053906
def main_a_np_pa_fr(puzzle_input):
    puzzle_lines = puzzle_input.read().splitlines()
    n_lines = len(puzzle_lines)

    left_list, right_list = np.zeros(n_lines), np.zeros(n_lines)
    for i, line in enumerate(puzzle_lines):
        a, b = line.split()
        left_list[i] = int(a)
        right_list[i] = int(b)

    left_list.sort()
    right_list.sort()
    return np.sum(np.abs(left_list - right_list))


def main_b(puzzle_input):
    left_list, right_list = [], []
    for line in puzzle_input:
        a, b = line.split()
        left_list.append(int(a))
        right_list.append(int(b))

    appearances_right_list = dict(zip(*np.unique(right_list, return_counts=True)))
    total_score = 0
    for number in left_list:
        try:
            total_score += appearances_right_list[number] * number
        except KeyError:
            pass

    return total_score


def benchmark(full_input, func):
    func(full_input)
    full_input.seek(0)


if __name__ == '__main__':
    EXAMPLE_MODE = False
    file_name = 'example.txt' if EXAMPLE_MODE else 'input.txt'
    code_to_test = main_a_np_pa_fr
    with open(file_name, 'r') as full_input:
        print("Functie", code_to_test.__name__, "runt 10000x in", timeit("benchmark(full_input, code_to_test)", globals=locals(), number=10000), "seconden.")
        # print(main_b(full_input))