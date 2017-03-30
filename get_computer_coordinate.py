import random


def get_computer_x(board_size, rows):
    for i in range(0, board_size):
        if rows[i] == ['X'] * 2 or rows[i] == ['O'] * 2:
            if i.index('X') == 0:
                x = i.index('X') + 1
                if rows[x] == 'X' or rows[x] == 'O':
                    x = i.index('X') + 2
            return x
        else:
            x = random.randrange(1, board_size)
            return x


def get_computer_y(board_size, rows):
    for i in range(0, board_size):
        if rows[i] == ['X'] * 2 or rows[i] == ['O'] * 2:
            if i.index('X') == 0:
                y = i.index('X') + 1
                if rows[y] == 'X' or rows[y] == 'O':
                    y = i.index('X') + 2
            return y
        else:
            y = random.randrange(1, board_size)
            return y
