def game_board(board_size):
    rows = []
    for i in range(0, board_size):
        row = []
        for i in range(0, board_size):
            row.append('_')
        rows.append(row)
    return rows
