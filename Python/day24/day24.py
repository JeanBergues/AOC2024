def main_a(puzzle_input):
    initial_states, gates = puzzle_input.read().split('\n\n')
    states = {l.split(':')[0]: int(l.split(':')[1].strip()) for l in initial_states.splitlines()}
    gates = gates.splitlines()
    
    while gates:
        unused_gates = []
        for gate in gates:
            in1, op, in2, _, out = gate.split(' ')
            if in1 not in states or in2 not in states:
                unused_gates.append(gate)
                continue
            if op == 'AND':
                states[out] = 1 if states[in1] == 1 and states[in2] == 1 else 0
            if op == 'OR':
                states[out] = 1 if states[in1] == 1 or states[in2] == 1 else 0
            if op == 'XOR':
                states[out] = 1 if states[in1] == 1 and states[in2] == 0 or states[in1] == 0 and states[in2] == 1 else 0

        gates = unused_gates
    
    z_list = [states[wire] for wire in sorted(states.keys()) if wire.startswith('z')]
    
    z_number = 0
    for i in range(len(z_list)):
        z_number += z_list[i] * (2**i)

    return z_number


def main_b(puzzle_input):

    return 0


if __name__ == '__main__':
    EXAMPLE_MODE = False
    file_name = 'example.txt' if EXAMPLE_MODE else 'input.txt'

    with open(file_name, 'r') as full_input:
        print(main_a(full_input))
        full_input.seek(0)
        print(main_b(full_input))