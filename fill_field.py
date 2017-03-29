import time


def fill_field(rows, x, y, player, player1):
    if rows[x - 1][y - 1] == '_':
        if player == player1:
            char = 'X'
        else:
            char = 'O'
        rows[x - 1][y - 1] = char
    else:
        print("Sorry, the field is reserved!")
        time.sleep(2)
        return False
    return
