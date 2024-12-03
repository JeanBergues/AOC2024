import re

def main_a(puzzle_input):
    total_result = 0
    instruction_string = puzzle_input.read()
    valid_mul_instructions = re.finditer("mul[(][0-9]+,[0-9]+[)]", instruction_string)

    for instruction in valid_mul_instructions:
        a, b = instruction.group()[4:-1].split(',')
        total_result += int(a) * int(b)

    return total_result


def main_b(puzzle_input):
    total_result = 0
    instruction_string = puzzle_input.read()
    valid_mul_instructions = re.finditer("mul[(][0-9]+,[0-9]+[)]", instruction_string)
    valid_do_instruction_ends = [0] + [match.span()[1] for match in re.finditer("do[(][)]", instruction_string)]
    valid_dont_instruction_ends = [match.span()[1] for match in re.finditer("don\'t[(][)]", instruction_string)]

    for instruction in valid_mul_instructions:
        mul_start_index = instruction.span()[0]
        a, b = instruction.group()[4:-1].split(',')

        last_do_index = [i for i in valid_do_instruction_ends if i <= mul_start_index][-1]
        last_dont_index = [i for i in valid_dont_instruction_ends if i <= mul_start_index][-1] if mul_start_index > valid_dont_instruction_ends[0] else -1
        if last_do_index > last_dont_index:
            total_result += int(a) * int(b)
        
    return total_result


if __name__ == '__main__':
    EXAMPLE_MODE = False
    with open('example.txt', 'r') if EXAMPLE_MODE else open('input.txt', 'r') as full_input:
        print(main_a(full_input))
    with open('example.txt', 'r') if EXAMPLE_MODE else open('input.txt', 'r') as full_input:
        print(main_b(full_input))