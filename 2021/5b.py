from aocd import lines, submit
from math import sqrt
import re

class VentMap:
    def __init__(self, lines):
        self.lines = []
        self.parse_lines(lines)
        self.map = [['.']]

    def parse_lines(self, lines):
        for line in lines:
            self.lines.append(Line(line))

    def resize_map(self, new_dim):
        size_delta = new_dim - len(self.map)
        extension = ['.'] * size_delta

        # extend existing rows
        for row in self.map:
            row.extend(extension)

        # add new rows
        new_row = ['.'] * new_dim
        self.map.extend([new_row.copy() for i in range(size_delta)])

    def map_lines(self):
        for line in self.lines:
            for coord in line:
                self[coord] += 1

    def count_overlaps(self):
        overlaps = 0
        for row in self.map:
            for pos in row:
                if pos != '.' and pos > 1:
                    overlaps += 1

        return overlaps

    def __getitem__(self, coord):
        x, y = coord

        if max(x, y) >= len(self.map):
            self.resize_map(max(x, y) + 1)

        return 0 if self.map[y][x] == '.' else self.map[y][x]

    def __setitem__(self, coord, value):
        x, y = coord

        if max(x, y) >= len(self.map):
            self.resize_map(max(x,y) + 1)

        self.map[y][x] = value

    def __str__(self):
        return '\n'.join([' '.join([str(pos) for pos in row]) for row in self.map])

class Line:
    def __init__(self, line_str):
        self.start = None
        self.end = None
        self.parse_line(line_str)
        
    def parse_line(self, line_str):
        line_pattern = "(\d+,\d+) -> (\d+,\d+)"
        line_matches = re.match(line_pattern, line_str)
        start_str, end_str = line_matches.groups()
        self.start, self.end = Coord(start_str), Coord(end_str)

    def __iter__(self):
        direction = self.end - self.start
        magnitude = sqrt(direction.x ** 2 + direction.y ** 2)
        normalized = direction / magnitude

        next_coord = Coord(f"{self.start.x}, {self.start.y}")
        while next_coord != self.end:
            yield next_coord
            next_coord += normalized
        
        yield next_coord

    def __repr__(self):
        return f"{self.start} -> {self.end}"

class Coord:
    def __init__(self, coord_str):
        x, y = coord_str.split(',')
        self.x = int(x)
        self.y = int(y)

    def __repr__(self):
        return f"{self.x},{self.y}"

    def __iter__(self):
        return iter((self.x, self.y))

    def __sub__(self, other):
        return Coord(f"{self.x - other.x}, {self.y - other.y}")

    def __add__(self, other):
        return Coord(f"{self.x + other.x}, {self.y + other.y}")

    def __iadd__(self, other):
        return self + other

    def __truediv__(self, value):
        return Coord(f"{round(self.x / value)}, {round(self.y / value)}")

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

def main():
    vm = VentMap(lines)

    vm.map_lines()

    submit(vm.count_overlaps())

if __name__ == '__main__':
    main()