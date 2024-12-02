import numpy as np


def check_level_safety(level_differences):
    max_difference = np.max(level_differences)
    min_difference = np.min(level_differences)
    
    if abs(max_difference) > 3 or abs(min_difference) > 3: 
        return False
    if min_difference * max_difference <= 0: 
        return False
    if np.isin(0, level_differences): 
        return False
    return True


def find_offending_levels(level_differences):
    level_direction = 1 if len(np.argwhere(level_differences > 0)) > (len(level_differences) / 2) else -1
    offending_indices = []
    for i, d in enumerate(level_differences):
        if d == 0: 
            offending_indices.append(i)
            continue
        if abs(d) > 3:
            offending_indices.append(i)
            continue
        if d * level_direction < 0: 
            offending_indices.append(i) 
            continue

    return offending_indices


def main_a(puzzle_input):
    safe_reports = 0
    for line in puzzle_input:
        report_array = np.fromstring(line, dtype=int, sep=' ')
        level_differences = np.diff(report_array, 1)
        if check_level_safety(level_differences):
            safe_reports += 1

    return safe_reports


def main_b(puzzle_input):
    safe_reports = 0

    for line in puzzle_input:
        report_array = np.fromstring(line, dtype=int, sep=' ')
        level_differences = np.diff(report_array, 1)

        if check_level_safety(level_differences):
            safe_reports += 1
        else:
            for i in range(len(report_array)):
                report_removed_inx = np.delete(report_array, i)
                level_diffs_removed_inx = np.diff(report_removed_inx, 1)
                
                if check_level_safety(level_diffs_removed_inx):
                    safe_reports += 1
                    break

    return safe_reports


if __name__ == '__main__':
    EXAMPLE_MODE = False
    with open('example.txt', 'r') if EXAMPLE_MODE else open('input.txt', 'r') as full_input:
        print(main_a(full_input))
    with open('example.txt', 'r') if EXAMPLE_MODE else open('input.txt', 'r') as full_input:
        print(main_b(full_input))