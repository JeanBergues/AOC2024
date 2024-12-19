import re

def possible_design(design, patterns):
    for p in patterns:
        if p == design:
            return True
        if len(p) > len(design):
            continue
        if re.match(p, design) == None:
            continue
        if possible_design(design[len(p):], patterns):
            return True

    return False


def total_designs(design, patterns, mem_dict):
    n_designs = 0

    if len(design) in mem_dict:
        return mem_dict[len(design)]
    
    for p in patterns:
        if p == design:
            n_designs += 1
            continue
        if len(p) > len(design):
            continue
        if re.match(p, design) == None:
            continue
        n_designs += total_designs(design[len(p):], patterns, mem_dict)

    mem_dict[len(design)] = n_designs
    return n_designs


def find_design_breakpoints(design, patterns):
    broken_strings = []
    from_i = 0
    for i in range(0, len(design)):
        pair = design[i:i+2]

        patterns_cointaining_pair = [p for p in patterns if re.search(pair, p) != None]
        useable_patterns = []

        for p in patterns_cointaining_pair:
            groups = [(m.start(), m.end()) for m in re.finditer(p, design) if m.start() <= i < m.end()]
            if len(groups) > 0:
                useable_patterns.append(p)

        print(pair, useable_patterns)

        if len(useable_patterns) == 0:
            broken_strings.append(design[from_i:i+1])
            from_i = i + 1

        if len(useable_patterns) == 1:
            correction = useable_patterns[0].find(pair)
            broken_strings.append(design[from_i-correction:i+1])
            from_i = i + 1

    broken_strings.append(design[from_i:])
    print(broken_strings)
    return broken_strings
        

def main_a(puzzle_input):
    patterns, designs = puzzle_input.read().split('\n\n')

    patterns = [p.strip() for p in patterns.split(',')]
    patterns.sort(key= lambda x: -1*len(x))
    designs = designs.splitlines()
    
    possible_designs = 0
    for design in designs:
        usable_patterns = [p for p in patterns if re.search(p, design) != None]
        if possible_design(design, usable_patterns): 
            possible_designs += 1

    return possible_designs


def main_b(puzzle_input):
    patterns, designs = puzzle_input.read().split('\n\n')

    patterns = [p.strip() for p in patterns.split(',')]
    patterns.sort(key= lambda x: -1*len(x))
    designs = designs.splitlines()
    
    n_designs = 0
    for design in designs:
        usable_patterns = [p for p in patterns if re.search(p, design) != None]
        n_designs += total_designs(design, usable_patterns, dict())

    return n_designs


if __name__ == '__main__':
    EXAMPLE_MODE = False
    file_name = 'example.txt' if EXAMPLE_MODE else 'input.txt'

    with open(file_name, 'r') as full_input:
        print(main_a(full_input))
        full_input.seek(0)
        print(main_b(full_input))