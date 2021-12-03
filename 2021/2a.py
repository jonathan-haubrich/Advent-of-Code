from aocd import lines, submit

class Submarine:
    MOVE_DICT = {
        "forward": lambda s, v: s.modify_horizontal_pos(int(v)),
        "down": lambda s, v: s.modify_depth(int(v)),
        "up": lambda s, v: s.modify_depth(-int(v)),
    }

    def __init__(self, move_list):
        self.move_list = move_list.copy()
        self.horizontal_pos = 0
        self.depth = 0

    def move(self):
        for move in self.move_list:
            self.modify_position(*move.split())

    def modify_horizontal_pos(self, v):
        self.horizontal_pos += v

    def modify_depth(self, v):
        self.depth += v

    def modify_position(self, move, value):
        Submarine.MOVE_DICT[move](self, value)

    def position(self):
        return self.horizontal_pos * self.depth


def main():
    s = Submarine(lines)
    s.move()
    submit(s.position())

if __name__ == '__main__':
    main()