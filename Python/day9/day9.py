def main_a(puzzle_input):
    file_array = []
    
    # Create diskmap
    for i, c in enumerate(puzzle_input.read()):
        for _ in range(int(c)):
            if i % 2 == 0:
                file_array.append(i // 2)
            else:
                file_array.append(None)

    #  Re-order diskmap
    for i in range(len(file_array) - file_array.count(None)):
        if file_array[i] == None:
            filled_value = False
            while not filled_value:
                new_file = file_array.pop()
                if new_file != None:
                    file_array[i] = new_file
                    filled_value = True

    # Calculate checksum
    checksum = 0
    for i, value in enumerate(file_array):
        checksum += i * value

    return checksum


def main_b(puzzle_input):
    file_array = []
    
    # Create diskmap
    for i, c in enumerate(puzzle_input.read()):
        if i % 2 == 0:
            file_array.append((i // 2, int(c)))
        elif int(c) > 0:
            file_array.append((None, int(c)))

    file_array_empty = False
    discard_pile = []
    while not file_array_empty:
        last_file = file_array[-1]
        if last_file[0] == None:
            discard_pile.append(last_file)
        else:
            moved_file = False
            for i in range(len(file_array)):
                empty_room = file_array[i]
                if empty_room[0] == None and empty_room[1] >= last_file[1]:
                    if empty_room[1] == last_file[1]:
                        file_array[i] = last_file
                    if empty_room[1] > last_file[1]:
                        file_array[i] = (None, empty_room[1] - last_file[1])
                        file_array.insert(i, last_file)

                    moved_file = True
                    break
                    
            if moved_file:
                discard_pile.append((None, last_file[1]))
            else:
                discard_pile.append(last_file)
            
        file_array.pop()
        if len(file_array) == 0:
            file_array_empty = True

    discard_pile.reverse()

    # Calculate checksum
    checksum = 0
    current_index = 0
    for file in discard_pile:
        if file[0] != None:
            for i in range(file[1]):
                checksum += (current_index + i) * file[0]

        current_index += file[1]

    return checksum


if __name__ == '__main__':
    EXAMPLE_MODE = False
    with open('example.txt', 'r') if EXAMPLE_MODE else open('input.txt', 'r') as full_input:
        print(main_a(full_input))
    with open('example.txt', 'r') if EXAMPLE_MODE else open('input.txt', 'r') as full_input:
        print(main_b(full_input))