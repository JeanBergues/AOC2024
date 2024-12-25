def simulate_system(wires, gates):
    while gates:
        unused_gates = []
        for gate in gates:
            in1, op, in2, _, out = gate.split(' ')
            if in1 not in wires or in2 not in wires:
                unused_gates.append(gate)
                continue
            if op == 'AND':
                wires[out] = 1 if wires[in1] == 1 and wires[in2] == 1 else 0
            if op == 'OR':
                wires[out] = 1 if wires[in1] == 1 or wires[in2] == 1 else 0
            if op == 'XOR':
                wires[out] = 1 if wires[in1] == 1 and wires[in2] == 0 or wires[in1] == 0 and wires[in2] == 1 else 0

        gates = unused_gates

    z_list = [wires[wire] for wire in sorted(wires.keys(), reverse=True) if wire.startswith('z')]
    return (wires, gates, z_list)


def convert_bitlist_to_integer(bitlist):
    result = 0
    for i, bit in enumerate(reversed(bitlist)):
        result += bit * (2**i)

    return result


def get_bitlist_from_integer(number, length=8):
    bits = list(map(int, bin(number)[2:]))

    return [0] * (length - len(bits)) + bits if length > len(bits) else bits


def main_a(puzzle_input):
    initial_states, gates = puzzle_input.read().split('\n\n')
    wires = {l.split(':')[0]: int(l.split(':')[1].strip()) for l in initial_states.splitlines()}
    gates = gates.splitlines()
    
    wires, gates, z_list = simulate_system(wires, gates)
    return convert_bitlist_to_integer(z_list)

# qwf, cnk, z14, vhm, z27, mps, z39, msq
# cnk,mps,msq,qwf,vhm,z14,z27,z39

def main_b_old(puzzle_input):
    # NUMBERS FOR TESTING
    X = 2 ** 44
    Y = 2 ** 44
    Z = X + Y
    N = 45

    # Load in the initial "wrong" state
    initial_states, gates = puzzle_input.read().split('\n\n')
    wires = {l.split(':')[0]: int(l.split(':')[1].strip()) for l in initial_states.splitlines()}
    gates = gates.splitlines()

    x_wires = [wire for wire in sorted(wires.keys(), reverse=True) if wire.startswith('x')]
    y_wires = [wire for wire in sorted(wires.keys(), reverse=True) if wire.startswith('y')]
    x_bits = get_bitlist_from_integer(X, length=N)
    y_bits = get_bitlist_from_integer(Y, length=N)
    correct_z = get_bitlist_from_integer(Z, length=N+1)
    
    # Load in the testing X's and Y's
    for i in range(N):
        wires[x_wires[i]] = x_bits[i]
        wires[y_wires[i]] = y_bits[i]
    
    z_list = simulate_system(wires, gates)[2]
    print(z_list)
    print(correct_z)
    print(convert_bitlist_to_integer(z_list))
    print(Z)
    
    return 0


def connected_to_via(inp, path_until_now, connections, known_paths):
    known_paths[inp] = path_until_now
    if not inp.startswith('z'):
        next_wires = [wire for wire in connections if inp in wire[0]]
        for wire in next_wires:
            connected_to_via(wire[2], path_until_now + [(wire[1], wire[2])], connections, known_paths)


def main_b(puzzle_input):
    # Load in the initial "wrong" state
    initial_states, gates = puzzle_input.read().split('\n\n')
    wires = {l.split(':')[0]: int(l.split(':')[1].strip()) for l in initial_states.splitlines()}
    gates = gates.splitlines()
    connections = []
    x_wires = [wire for wire in sorted(wires.keys(), reverse=True) if wire.startswith('x')]

    for gate in gates:
        in1, op, in2, _, out = gate.split(' ')
        connections.append(([in1, in2], op, out))

    incorrect_outs = set()
    out_dict = {}
    for x in x_wires:
        paths = dict()
        xnum = int(x[1:])
        connected_to_via(x, [], connections, paths)
        trouble_reaching = []
        first_trouble = []
        found_trouble = False
        for k, v in sorted(paths.items()):
            if k.startswith('z'):
                znum = int(k[1:])
                expected = ['AND', 'OR'] * (znum - xnum) + ['XOR']
                if xnum == znum: expected += ['XOR']
                if znum == 45: expected.pop()
                if xnum == 0 and znum == 0: expected = ['XOR']
                path_to = [p[0] for p in v]

                if path_to != expected:
                    expected.insert(0, 'XOR')
                    if path_to != expected:
                    # print(xnum, znum)
                        trouble_reaching.append(znum)
                        if not found_trouble:
                            first_trouble = v
                            found_trouble = True

                    # print(expected) 
                    # print(path_to)
                    # print(v)
                    # print()

                # i = 0
                # correction = 0
                # while i < min(len(expected), len(path_to)):
                #     if expected[i] != path_to[i]:
                #         print(i)
                #         print(expected)
                #         print(path_to)
                        
                #         if len(expected) == len(path_to):
                #             expected.pop(i)
                #             path_to.pop(i)
                #             i = i - 1
                #             correction += 1
                #         elif len(expected) > len(path_to):
                #             expected.pop(i)
                #             i = i - 1
                #         elif len(expected) < len(path_to):
                #             path_to.pop(i)
                #             i = i - 1
                #             correction += 1
                #         # print(expected)
                #         # print(path_to)
                #         incorrect_outs.add(v[i + correction][1])
                #         out_dict[v[i + correction][1]] = out_dict.get(v[i + correction][1], 0) + 1
                #         break
                #         # print(v[i + correction][1])
                #         # print('\n\n')
                #     i += 1
        # print(f"{xnum} has trouble reaching {trouble_reaching}")
        # print(first_trouble)
        # print()
    
    return 0


if __name__ == '__main__':
    EXAMPLE_MODE = False
    file_name = 'example.txt' if EXAMPLE_MODE else 'input.txt'

    with open(file_name, 'r') as full_input:
        # print(main_a(full_input))
        # full_input.seek(0)
        print(main_b(full_input))
        full_input.seek(0)
        print(main_b_old(full_input))

# msq, z39, z27, mps, z14, vhm