from aocd import lines, submit

class BingoPuzzle:
    def __init__(self, lines):
        self.numbers = lines[0].split(',')
        self.boards = []
        self.parse_lines(lines)

    def parse_lines(self, lines):
        for i in range(1, len(lines), 6):
            self.boards.append(BingoBoard(lines[i:i+6]))

class BingoBoard:
    def __init__(self, lines):
        self.board = []
        for row in lines[1:]:
            self.board.append([BingoBoardPosition(number) for number in row.split()])

    def is_winning_row(self, row):
        for position in row:
            if not position.marked:
                return False
        
        return row

    def is_winning_column(self, column):
        for row in self.board:
            if not row[column].marked:
                return False

        return [row[column] for row in self.board]

    def is_winner(self):
        for row in self.board:
            if self.is_winning_row(row):
                return True
        
        for column in range(len(self.board[0])):
            if self.is_winning_column(column):
                return True

        return False

    def mark_position(self, position):
        for row in self.board:
            for pos in row:
                if pos == position:
                    pos.mark()

    def calculate_score(self, called_number):
        score = 0
        for row in self.board:
            for position in row:
                if not position.marked:
                    score += int(position)

        return score * int(called_number)

    def __str__(self):
        return '\n'.join([' '.join([str(pos) for pos in row]) for row in self.board])

class BingoBoardPosition:
    def __init__(self, number):
        self.number = number
        self.marked = False

    def mark(self):
        self.marked = True

    def __str__(self):
        return str(self.number)

    def __repr__(self):
        return str(self)

    def __eq__(self, other):
        return self.number == other

    def __int__(self):
        return int(self.number)


def main():
    bp = BingoPuzzle(lines)

    for number in bp.numbers:
        for board in bp.boards:
            board.mark_position(number)
            if board.is_winner():
                submit(board.calculate_score(number))
                return

if __name__ == '__main__':
    main()