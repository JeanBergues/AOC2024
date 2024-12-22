from itertools import product

def mix(secret, value):
    return secret ^ value

def prune(secret):
    return secret % 16777216

def next_secret(secret):
    result = prune(mix(secret, secret * 64))
    result = prune(mix(result, result // 32))
    result = prune(mix(result, result * 2048))
    return result

def main_a(puzzle_input):
    total = 0

    for line in puzzle_input:
        secret = int(line.strip())
        for _ in range(2000):
            secret = next_secret(secret)
        total += secret
    
    return total


def main_b(puzzle_input):
    best_total = 0
    secret_seq_dicts = []

    for line in puzzle_input:
        last_4_secret_changes = []
        secret = int(line.strip())
        current_total = 0
        sequences = dict()

        for _ in range(2000):
            next_s = next_secret(secret)
            last_4_secret_changes.append(next_s % 10 - secret % 10)
            if len(last_4_secret_changes) > 4:
                last_4_secret_changes.pop(0)
                if tuple(last_4_secret_changes) not in sequences:
                    sequences[tuple(last_4_secret_changes)] = next_s % 10
            secret = next_s
        secret_seq_dicts.append(sequences)

    for sequence_tuple in product(range(-9, 10), repeat=4):
        if sum(sequence_tuple) <= 0 or sum(sequence_tuple) > 9:
            continue

        current_total = 0
        for s in secret_seq_dicts:
            current_total += s.get(sequence_tuple, 0)

        if current_total > best_total: 
            best_total = current_total
            print(sequence_tuple)
    
    return best_total


if __name__ == '__main__':
    EXAMPLE_MODE = False
    file_name = 'example.txt' if EXAMPLE_MODE else 'input.txt'

    with open(file_name, 'r') as full_input:
        # print(main_a(full_input))
        # full_input.seek(0)
        print(main_b(full_input))