import numpy as np

def main_a(puzzle_input):
    current_state = list(map(int, puzzle_input.read().strip().split()))
    N_BLINKS = 25

    for i in range(N_BLINKS):
        print(f"Iteration {i}")
        new_state = []
        for stone in current_state:
            if stone == 0:
                new_state.append(1)
            elif len(str(stone)) % 2 == 0:
                new_state.append(int(str(stone)[0:(len(str(stone)) // 2)]))
                new_state.append(int(str(stone)[(len(str(stone)) // 2):]))
            else:
                new_state.append(stone * 2024)

        current_state = new_state

    return len(current_state)


def main_b(puzzle_input):
    current_state = list(map(int, puzzle_input.read().strip().split()))
    state_dict = {}
    for stone in current_state:
        state_dict[stone] = state_dict.get(stone, 0) + 1

    N_BLINKS = 75
    for _ in range(N_BLINKS):
        new_state_dict = state_dict.copy()
        for stone, amount in state_dict.items():
            if stone == 0:
                new_state_dict[1] = new_state_dict.get(1, 0) + amount
            elif len(str(stone)) % 2 == 0:
                left, right = int(str(stone)[0:(len(str(stone)) // 2)]), int(str(stone)[(len(str(stone)) // 2):])
                new_state_dict[left] = new_state_dict.get(left, 0) + amount
                new_state_dict[right] = new_state_dict.get(right, 0) + amount
            else:
                new_state_dict[stone * 2024] = new_state_dict.get(stone * 2024, 0) + amount
            new_state_dict[stone] = new_state_dict.get(stone, amount) - amount

        state_dict = new_state_dict

    # for k, v in state_dict.items():
    #     if v != 0:
    #         print(k, v)

    return sum(state_dict.values())

if __name__ == '__main__':
    EXAMPLE_MODE = False
    # with open('example.txt', 'r') if EXAMPLE_MODE else open('input.txt', 'r') as full_input:
    #     print(main_a(full_input))
    with open('example.txt', 'r') if EXAMPLE_MODE else open('input.txt', 'r') as full_input:
        print(main_b(full_input))