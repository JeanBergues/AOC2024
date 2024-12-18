def main_a(puzzle_input):
    full_input = puzzle_input.read().splitlines()
    
    A = int(full_input[0].split(':')[1].strip())
    B = int(full_input[1].split(':')[1].strip())
    C = int(full_input[2].split(':')[1].strip())
    program = list(map(int, full_input[4].split(':')[1].strip().split(',')))
    
    instruction_pointer = 0
    program_output = []

    while instruction_pointer < len(program):
        JUMPED = False
        # Read in the full instruction
        instruction = program[instruction_pointer]
        literal_operand = program[instruction_pointer + 1]
        if literal_operand <= 3:
            combo_operand = literal_operand
        if literal_operand == 4:
            combo_operand = A
        if literal_operand == 5:
            combo_operand = B
        if literal_operand == 6:
            combo_operand = C

        # Perform the instruction
        if instruction == 0: #ADV
            A = A // (2**combo_operand)
        if instruction == 1: #BXL
            B = B ^ literal_operand
        if instruction == 2: #BST
            B = combo_operand % 8
        if instruction == 3: #JNZ
            if A != 0:
                instruction_pointer = literal_operand
                JUMPED = True
        if instruction == 4: #BXC
            B = B ^ C
        if instruction == 5: #OUT
            program_output.append(combo_operand % 8)
        if instruction == 6: #BDV
            B = A // (2**combo_operand)
        if instruction == 7: #CDV
            C = A // (2**combo_operand)

        if not JUMPED:
            instruction_pointer += 2

        # print(instruction, literal_operand, combo_operand)
        # print(A, B, C)
        # print()

    output_string = ""
    for out in program_output:
        output_string += str(out) + ','

    return output_string


def main_b_old(puzzle_input):
    full_input = puzzle_input.read().splitlines()
    
    initial_A = 205952832774415
    B = int(full_input[1].split(':')[1].strip())
    C = int(full_input[2].split(':')[1].strip())
    program = list(map(int, full_input[4].split(':')[1].strip().split(',')))

    EQUAL_PROGRAM = False
    while not EQUAL_PROGRAM:
        if initial_A % 10000 == 0: print("Checking A=", initial_A)
        A = initial_A
        instruction_pointer = 0
        program_output = []

        if not A_is_viable(initial_A, program[0]): continue

        while instruction_pointer < len(program):
            JUMPED = False
            # Read in the full instruction
            instruction = program[instruction_pointer]
            literal_operand = program[instruction_pointer + 1]
            if literal_operand <= 3:
                combo_operand = literal_operand
            if literal_operand == 4:
                combo_operand = A
            if literal_operand == 5:
                combo_operand = B
            if literal_operand == 6:
                combo_operand = C

            # Perform the instruction
            if instruction == 0: #ADV
                A = A // (2**combo_operand)
            if instruction == 1: #BXL
                B = B ^ literal_operand
            if instruction == 2: #BST
                B = combo_operand % 8
            if instruction == 3: #JNZ
                if A != 0:
                    instruction_pointer = literal_operand
                    JUMPED = True
            if instruction == 4: #BXC
                B = B ^ C
            if instruction == 5: #OUT
                out = combo_operand % 8
                if out != program[len(program_output)]:
                    break
                program_output.append(out)
            if instruction == 6: #BDV
                B = A // (2**combo_operand)
            if instruction == 7: #CDV
                C = A // (2**combo_operand)

            if not JUMPED:
                instruction_pointer += 2
            
        if program_output == program:
            EQUAL_PROGRAM = True
        else:
            initial_A += 1

    return A

def A_is_viable(A, out):
    B = (A % 8)         # 2, 4
    B = B ^ 5           # 1, 5
    C = A // (2 ** B)   # 7, 5
    B = B ^ 6           # 1, 6
    B = B ^ C           # 4, 1

    return B % 8 == out


def find_recursive(i, output, A):
    if i == -1:
        return A // 8
    
    for test_A in range(A, A + 8):
        B = (test_A % 8)        # 2, 4
        B = B ^ 5               # 1, 5
        C = test_A // (2 ** B)  # 7, 5
        B = B ^ 6               # 1, 6
        B = B ^ C               # 4, 1

        if B % 8 == output[i]:
            other_A = find_recursive(i - 1, output, test_A * 8)
            if other_A != None:
                return other_A 
    
    return None


def main_b(puzzle_input):
    full_input = puzzle_input.read().splitlines()
    program = list(map(int, full_input[4].split(':')[1].strip().split(',')))

    A_needed = find_recursive(len(program) - 1, program, 0)

    return A_needed


if __name__ == '__main__':
    EXAMPLE_MODE = False
    with open('example.txt', 'r') if EXAMPLE_MODE else open('input.txt', 'r') as full_input:
        print(main_a(full_input))
    with open('example.txt', 'r') if EXAMPLE_MODE else open('input.txt', 'r') as full_input:
        print(main_b(full_input))