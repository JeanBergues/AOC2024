def main_a(puzzle_input):
    MAX_PRESSES = 100
    total_tokens = 0

    for configuration in puzzle_input.read().split('\n\n'):
        
        current_config = configuration.split('\n')
        XA, YA = int(current_config[0].split('+')[1].split(',')[0]), int(current_config[0].split('+')[2].strip())
        XB, YB = int(current_config[1].split('+')[1].split(',')[0]), int(current_config[1].split('+')[2].strip())
        XP, YP = int(current_config[2].split('=')[1].split(',')[0]), int(current_config[2].split('=')[2].strip())

        for a_presses in range(MAX_PRESSES):
            if (XP - a_presses * XA) % XB == 0:
                b_presses = (XP - a_presses * XA) // XB
                if b_presses * YB + a_presses * YA == YP:
                    total_tokens += a_presses * 3 + b_presses
                    break
            
    return total_tokens


def main_b(puzzle_input):
    total_tokens = 0
    extra_factor = 10000000000000

    for configuration in puzzle_input.read().split('\n\n'):
        
        current_config = configuration.split('\n')
        XA, YA = int(current_config[0].split('+')[1].split(',')[0]), int(current_config[0].split('+')[2].strip())
        XB, YB = int(current_config[1].split('+')[1].split(',')[0]), int(current_config[1].split('+')[2].strip())
        XP, YP = int(current_config[2].split('=')[1].split(',')[0]), int(current_config[2].split('=')[2].strip())
        
        XP += extra_factor
        YP += extra_factor

        # Using Cramers rule
        Delta = XA * YB - XB * YA
        Delta1 = XP * YB - YP * XB
        Delta2 = XA * YP - YA * XP
        
        if Delta1 % Delta == 0 and Delta2 % Delta == 0:
            total_tokens += 3 * (Delta1 // Delta) + (Delta2 // Delta)
            print((Delta1 // Delta), (Delta2 // Delta))
            
    return total_tokens


if __name__ == '__main__':
    EXAMPLE_MODE = False
    with open('example.txt', 'r') if EXAMPLE_MODE else open('input_Sven.txt', 'r') as full_input:
        print(main_a(full_input))
    with open('example.txt', 'r') if EXAMPLE_MODE else open('input_Sven.txt', 'r') as full_input:
        print(main_b(full_input))