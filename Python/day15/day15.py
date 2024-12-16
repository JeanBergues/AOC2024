def main_a(puzzle_input):
    positions, moves = puzzle_input.read().split('\n\n')
    moves = moves.strip()

    movement_dict = {
        '^': (0, -1),
        'v': (0, 1),
        '<': (-1, 0),
        '>': (1, 0)
    }

    walls = set()
    boxes = set()
    robot = (0, 0)
    for y, row in enumerate(positions.splitlines()):
        for x, c in enumerate(row):
            if c == '#':
                walls.add((x, y))
            elif c == 'O':
                boxes.add((x, y))
            elif c == '@':
                robot = (x, y)

    for move in moves:
        if move == '\n': continue
        step = movement_dict[move]
        next_pos = (robot[0] + step[0], robot[1] + step[1])
        if next_pos in walls:
            continue
        elif next_pos in boxes:
            next_box_pos = (next_pos[0] + step[0], next_pos[1] + step[1])
            end_of_boxes = False
            while not end_of_boxes:
                if next_box_pos in walls:
                    break
                elif next_box_pos not in boxes:
                    end_of_boxes = True
                else:
                    next_box_pos = (next_box_pos[0] + step[0], next_box_pos[1] + step[1])
            
            if end_of_boxes == False: continue
            boxes.add(next_box_pos)
            boxes.remove(next_pos)

        robot = next_pos

    coordinate_sum = 0
    for box in boxes:
        coordinate_sum += box[0] + 100 * box[1]

    return coordinate_sum


def vertical_check(check_pos, step, walls, boxes):
    boxes_to_move = set()
    l, r = (check_pos[0], check_pos[2] + step[1]), (check_pos[1], check_pos[2] + step[1])
    check_u_position = (check_pos[0], check_pos[1], check_pos[2] + step[1])
    check_l_position = (check_pos[0] - 1, check_pos[1] - 1, check_pos[2] + step[1])
    check_r_position = (check_pos[0] + 1, check_pos[1] + 1, check_pos[2] + step[1])

    if l in walls or r in walls:
        boxes_to_move.add(None)
        return boxes_to_move
    if check_u_position in boxes:
        boxes_to_move.add(check_u_position)
        boxes_to_move |= vertical_check(check_u_position, step, walls, boxes)
    if check_l_position in boxes:
        boxes_to_move.add(check_l_position)
        boxes_to_move |= vertical_check(check_l_position, step, walls, boxes)
    if check_r_position in boxes:
        boxes_to_move.add(check_r_position)
        boxes_to_move |= vertical_check(check_r_position, step, walls, boxes)
    
    boxes_to_move.add(check_pos)
    return boxes_to_move


def pretty_print(robot, boxes, walls, dims):
    str_array = []
    for _ in range(dims[1]):
        str_array.append(["."]*dims[0])

    str_array[robot[1]][robot[0]] = '@'
    for x, y in walls:
        str_array[y][x] = '#'

    for x1, x2, y in boxes:
        str_array[y][x1] = '['
        str_array[y][x2] = ']'

    final_str = ""
    for s in str_array:
        final_str += "".join(s) + '\n'

    print(final_str)

def main_b(puzzle_input):
    positions, moves = puzzle_input.read().split('\n\n')
    moves = moves.strip()

    movement_dict = {
        '^': (0, -1),
        'v': (0, 1),
        '<': (-1, 0),
        '>': (1, 0)
    }

    box_movement_dict = {
        '^': (0, 1, -1),
        'v': (0, 1, 1),
        '<': (-2, -1, 0),
        '>': (1, 2, 0)
    }

    walls = set()
    boxes = set()
    robot = (0, 0)
    xdim, ydim = 0, 0

    for y, row in enumerate(positions.splitlines()):
        ydim = y + 1
        for x, c in enumerate(row):
            xdim = 2*(x + 1)
            if c == '#':
                walls.add((2*x, y))
                walls.add((2*x + 1, y))
            elif c == 'O':
                boxes.add((2*x, 2*x+1, y))
            elif c == '@':
                robot = (2*x, y)

    pretty_print(robot, boxes, walls, (xdim, ydim))

    for move in moves:
        # input()
        if move == '\n': continue

        step = movement_dict[move]
        box_check_step = box_movement_dict[move]
        next_pos = (robot[0] + step[0], robot[1] + step[1])
        check_pos = (robot[0] + box_check_step[0], robot[0] + box_check_step[1], robot[1] + box_check_step[2])
        if next_pos in walls:
            print(move, "- GAAT NIET")
            continue

        elif check_pos in boxes and step[1] == 0:
            boxes_to_move = set()
            end_of_boxes = False

            while not end_of_boxes:
                l, r = (check_pos[0], check_pos[2]), (check_pos[1], check_pos[2])
                if l in walls and r in walls:
                    break
                elif l in walls or r in walls:
                    end_of_boxes = True
                elif check_pos not in boxes:
                    end_of_boxes = True
                else:
                    boxes_to_move.add(check_pos)
                    check_pos = (check_pos[0] + 2*step[0], check_pos[1] + 2*step[0], check_pos[2])
            
            if end_of_boxes == False:
                print(move, "- GAAT NIET") 
                continue
            
            for box in boxes_to_move:
                boxes.remove(box)
            for box in boxes_to_move:
                boxes.add((box[0] + step[0], box[1] + step[0], box[2] + step[1]))

        elif check_pos in boxes and step[0] == 0:
            boxes_to_move = vertical_check(check_pos, step, walls, boxes)
            print(boxes_to_move)
            if None in boxes_to_move:
                print(move, "- GAAT NIET")
                continue
            else:
                for box in boxes_to_move:
                    boxes.remove(box)
                for box in boxes_to_move:
                    boxes.add((box[0] + step[0], box[1] + step[0], box[2] + step[1]))

        elif (check_pos[0] - 1, check_pos[1] - 1, check_pos[2]) in boxes and step[0] == 0:
            boxes_to_move = vertical_check((check_pos[0] - 1, check_pos[1] - 1, check_pos[2]), step, walls, boxes)
            print(boxes_to_move)
            if None in boxes_to_move:
                print(move, "- GAAT NIET")
                continue
            else:
                for box in boxes_to_move:
                    boxes.remove(box)
                for box in boxes_to_move:
                    boxes.add((box[0] + step[0], box[1] + step[0], box[2] + step[1]))

        robot = next_pos
        # print(robot)
        # print(boxes)
        print(move)
        # pretty_print(robot, boxes, walls, (xdim, ydim))
        

    coordinate_sum = 0
    for box in boxes:
        coordinate_sum += box[0] + 100 * box[2]

    return coordinate_sum


if __name__ == '__main__':
    EXAMPLE_MODE = False
    with open('example.txt', 'r') if EXAMPLE_MODE else open('input.txt', 'r') as full_input:
        print(main_a(full_input))
    with open('example.txt', 'r') if EXAMPLE_MODE else open('input.txt', 'r') as full_input:
        print(main_b(full_input))