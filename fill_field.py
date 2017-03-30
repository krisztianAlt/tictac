
def fill_field(rows, x, y, player, player1):
    if rows[x - 1][y - 1] == '_':
        if player == player1:
            char = 'X'
        else:
            char = 'O'
        rows[x - 1][y - 1] = char
    else:
        return False
    return
