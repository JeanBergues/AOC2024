class Coordinate:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Coordinate(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other):
        return Coordinate(self.x - other.x, self.y - other.y)
    
    def __mul__(self, k):
        return Coordinate(self.x * k, self.y * k)
    
    def __str__(self):
        return f"({self.x}, {self.y})"
    
    def __ge__(self, other):
        return self.x >= other.x and self.y >= other.y
    
    def __le__(self, other):
        return self.x <= other.x and self.y <= other.y
    
    def magnitude(self):
        return (self.x * self.x + self.y * self.y) ** 0.5


def main_a(puzzle_input):
    unique_antinodes = set()
    coordinate_dict = {}
    origin = Coordinate(0, 0)

    for y, row in enumerate(puzzle_input):
        for x, c in enumerate(list(row.strip())):
            BOUND = Coordinate(len(row) -1, len(row) -1)
            if c != '.':
                if c not in coordinate_dict:
                    coordinate_dict[c] = [Coordinate(x, y)]
                else:
                    coordinate_dict[c].append(Coordinate(x, y))

    for antennas in coordinate_dict.values():
        for i in range(len(antennas) - 1):
            for j in range(i+1, len(antennas)):
                a1, a2 = antennas[i], antennas[j]
                delta = a1 - a2
                an1 = a1 - delta
                an2 = a2 + delta
                
                if origin <= an1 <= BOUND:
                    unique_antinodes.add(an1)
                if origin <= an2 <= BOUND:
                    unique_antinodes.add(an2)

    return len(unique_antinodes)


def main_b(puzzle_input):
    unique_antinodes = set()
    coordinate_dict = {}
    origin = Coordinate(0, 0)

    for y, row in enumerate(puzzle_input):
        for x, c in enumerate(list(row.strip())):
            BOUND = Coordinate(len(row) -1, len(row) -1)
            if c != '.':
                if c not in coordinate_dict:
                    coordinate_dict[c] = [Coordinate(x, y)]
                else:
                    coordinate_dict[c].append(Coordinate(x, y))

    for antennas in coordinate_dict.values():
        for i in range(len(antennas)):
            for j in range(i+1, len(antennas)):
                a1, a2 = antennas[i], antennas[j]
                delta = a2 - a1

                out_of_bounds = False
                k = 0
                while not out_of_bounds:
                    an = a1 - delta * k
                    if origin <= an <= BOUND:
                        unique_antinodes.add(an)
                        k += 1
                    else:
                        out_of_bounds = True

                out_of_bounds = False
                k = 1
                while not out_of_bounds:
                    an = a1 + delta * k
                    if origin <= an <= BOUND:
                        unique_antinodes.add(an)
                        k += 1
                    else:
                        out_of_bounds = True

    return len(unique_antinodes)


if __name__ == '__main__':
    EXAMPLE_MODE = True
    with open('example.txt', 'r') if EXAMPLE_MODE else open('input.txt', 'r') as full_input:
        print(main_a(full_input))
    with open('example.txt', 'r') if EXAMPLE_MODE else open('input.txt', 'r') as full_input:
        print(main_b(full_input))