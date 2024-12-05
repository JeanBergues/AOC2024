def check_page_correctness(update_array, relevant_rules):
    for i, page_number in enumerate(update_array):
        for rule in relevant_rules:
            if rule[0] == page_number and rule[1] in update_array[:i]:
                return False
            if rule[1] == page_number and rule[0] in update_array[i+1:]:
                return False

    return True

def main_a(puzzle_input):
    total = 0
    ordering_rules, page_numbers = puzzle_input.read().split('\n\n')

    rule_array = []
    for rule in ordering_rules.split('\n'):
        rule_array.append(list(map(int, rule.split('|'))))
    
    for update in page_numbers.split('\n'):
        update_array = [int(x) for x in update.split(',')]

        relevant_rules = []
        for rule in rule_array:
            if rule[0] in update_array and rule[1] in update_array:
                relevant_rules.append(rule)

        if check_page_correctness(update_array, relevant_rules): total += update_array[len(update_array) // 2]
    
    return total


def main_b(puzzle_input):
    total = 0
    ordering_rules, page_numbers = puzzle_input.read().split('\n\n')

    rule_array = []
    for rule in ordering_rules.split('\n'):
        rule_array.append(list(map(int, rule.split('|'))))
    
    for update in page_numbers.split('\n'):
        update_array = [int(x) for x in update.split(',')]

        relevant_rules = []
        for rule in rule_array:
            if rule[0] in update_array and rule[1] in update_array:
                relevant_rules.append(rule)

        if check_page_correctness(update_array, relevant_rules): continue

        right_rule_column = [x[1] for x in relevant_rules] # Hier wel relevant rules zetten anders werkt ie niet JAN
        page_number_counts = {k: right_rule_column.count(k) for k in update_array}
        corrected_update = [x[0] for x in sorted(page_number_counts.items(), key=lambda x:x[1])]

        total += corrected_update[len(update_array) // 2]
    
    return total


if __name__ == '__main__':
    EXAMPLE_MODE = False
    with open('example.txt', 'r') if EXAMPLE_MODE else open('input.txt', 'r') as full_input:
        print(main_a(full_input))
    with open('example.txt', 'r') if EXAMPLE_MODE else open('input.txt', 'r') as full_input:
        print(main_b(full_input))

# rule_is_correct = False
# new_update = update_array.copy()
# while not rule_is_correct:
#     for i, page_number in enumerate(update_array):
#         for rule in relevant_rules:
#             if (rule[0] == page_number and rule[1] in update_array[:i]):
#                 a, b = update_array.index(rule[0]), update_array.index(rule[1])
#                 new_update[a], new_update[b] = new_update[b], new_update[a]

#             if (rule[1] == page_number and rule[0] in update_array[i+1:]):
#                 a, b = update_array.index(rule[0]), update_array.index(rule[1])
#                 new_update[a], new_update[b] = new_update[b], new_update[a]

#     rule_is_correct = check_page_correctness(new_update, relevant_rules)

# if not check_page_correctness(corrected_update, relevant_rules):
#     rule_is_correct = False
#     new_update = corrected_update.copy()
#     while not rule_is_correct:
#         for i, page_number in enumerate(update_array):
#             for rule in relevant_rules:
#                 if (rule[0] == page_number and rule[1] in new_update[:i]):
#                     a, b = new_update.index(rule[0]), new_update.index(rule[1])
#                     new_update[a], new_update[b] = new_update[b], new_update[a]
#                     print(rule[0], rule[1])
#                     print(a)
#                     print(new_update)
#                     print('-')

#         rule_is_correct = check_page_correctness(new_update, relevant_rules)

#     total += new_update[len(update_array) // 2]
#     return 0

# else: 