import numpy as np


def main_a(puzzle_input):
    left_list, right_list = [], []
    for line in puzzle_input:
        a, b = line.split()
        left_list.append(int(a))
        right_list.append(int(b))

    left_list.sort()
    right_list.sort()
    return np.sum(np.abs(np.array(left_list) - np.array(right_list)))


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


if __name__ == '__main__':
    EXAMPLE_MODE = False
    with open('example.txt', 'r') if EXAMPLE_MODE else open('input.txt') as full_input:
        print(main_a(full_input))
    with open('example.txt', 'r') if EXAMPLE_MODE else open('input.txt') as full_input:
        print(main_b(full_input))