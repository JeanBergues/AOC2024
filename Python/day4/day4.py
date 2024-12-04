import re
import numpy as np


def create_diagonal_like_search(word_search, placehold_character = '-', from_upper_left = True):
    diag_word_search = []
    dim = len(word_search)
    for i, line in enumerate(word_search):
        if from_upper_left:
            new_line = [placehold_character] * (i) + line + [placehold_character] * (dim-i-1)
        else:
            new_line = [placehold_character] * (dim-i-1) + line + [placehold_character] * (i)
        diag_word_search.append(new_line)

    return diag_word_search


def search_columns_word_search(word_search):
    count = 0
    word_search_array = np.array(word_search)
    for i in range(len(word_search[0])):
        column = "".join(word_search_array[:,i])
        count += len(re.findall("XMAS", column))
        count += len(re.findall("SAMX", column))

    return count


def main_a(puzzle_input):
    xmas_appearances = 0
    word_search = []
    
    for line in puzzle_input:
        word_search.append(list(line.strip()))
        xmas_appearances += len(re.findall("XMAS", line))
        xmas_appearances += len(re.findall("SAMX", line))

    xmas_appearances += search_columns_word_search(word_search)
    xmas_appearances += search_columns_word_search(create_diagonal_like_search(word_search, from_upper_left=True))
    xmas_appearances += search_columns_word_search(create_diagonal_like_search(word_search, from_upper_left=False))
    
    return xmas_appearances


def main_b(puzzle_input):
    mas_appearances = 0
    word_search = []
    
    for line in puzzle_input:
        word_search.append(list(line.strip()))

    word_search_array = np.array(word_search)
    for i in range(1, len(word_search)-1):
        for j in range(1, len(word_search)-1):
            if word_search_array[i, j] == 'A':
                nw = word_search_array[i-1, j-1]
                se = word_search_array[i+1, j+1]

                if (nw == 'M' and se == 'S') or (nw == 'S' and se == 'M'):
                    ne = word_search_array[i-1, j+1]
                    sw = word_search_array[i+1, j-1]

                    if (ne == 'M' and sw == 'S') or (ne == 'S' and sw == 'M'): mas_appearances += 1
                        
    return mas_appearances


if __name__ == '__main__':
    EXAMPLE_MODE = False
    with open('example.txt', 'r') if EXAMPLE_MODE else open('input.txt', 'r') as full_input:
        print(main_a(full_input))
    with open('example.txt', 'r') if EXAMPLE_MODE else open('input.txt', 'r') as full_input:
        print(main_b(full_input))