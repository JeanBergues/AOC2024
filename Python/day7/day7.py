from sympy.utilities.iterables import multiset_permutations

def main_a(puzzle_input):
    total_result = 0

    for line in puzzle_input:
        answer, equation_text = line.split(':')
        answer = int(answer)
        equation = list(map(int, equation_text.split(' ')[1:]))

        operands = len(equation) - 1
        start_value = equation[0]

        for operators in multiset_permutations([True] * operands + [False] * operands, operands):
            current_value = start_value
            for i, operation in enumerate(operators):
                current_value = current_value + equation[i+1] if operation else current_value * equation[i+1]
                if current_value > answer:
                    break

            if current_value == answer:
                total_result += answer
                break

    return total_result


def main_b(puzzle_input):
    total_result = 0

    for line in puzzle_input:
        answer, equation_text = line.split(':')
        answer = int(answer)
        equation = list(map(int, equation_text.split(' ')[1:]))

        operands = len(equation) - 1
        start_value = equation[0]

        for operators in multiset_permutations(['+'] * operands + ['*'] * operands + ['|'] * operands, operands):
            current_value = start_value
            for i, operation in enumerate(operators):
                if operation == '+':
                    current_value += equation[i+1]
                if operation == '*':
                    current_value *= equation[i+1]
                if operation == '|':
                    current_value = int(str(current_value) + str(equation[i+1]))
                
                if current_value > answer:
                    break

            if current_value == answer:
                total_result += answer
                break

    return total_result


if __name__ == '__main__':
    EXAMPLE_MODE = False
    # with open('example.txt', 'r') if EXAMPLE_MODE else open('input.txt', 'r') as full_input:
    #     print(main_a(full_input))
    with open('example.txt', 'r') if EXAMPLE_MODE else open('input.txt', 'r') as full_input:
        print(main_b(full_input))