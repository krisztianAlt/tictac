def computer_check():

    for i in range(0, board_size):
            if rows[i] == ['X'] * board_size - 1:
                return "computer_attack"
            if rows[i] == ['O'] * board_size - 1:
                return "computer_WantWin"
        for i in range(0, board_size):
            s = []
            for e in range(0, board_size):
                s.append(rows[e][i])
            if s == ['X'] * board_size-1:
                return "computer_attack"
            if s == ['O'] * board_size-1:
                return "computer_WantWin"
        s = []
        for e in range(0, board_size):
            s.append(rows[e][e])
        if s == ['X'] * board_size-1:
            return "computer_attack"
        if s == ['O'] * board_size-1:
            return "computer_WantWin"
        s = []
        y_koord = board_size - 1
        for i in range(0, board_size):
            s.append(rows[i][y_koord])
            y_koord = y_koord - 1
        if s == ['X'] * board_size-1:
            return "computer_attack"
        if s == ['O'] * board_size-1:
            return "computer_WantWin"
        draw_check = 0
        for row in rows:
            if '_' in row:
                draw_check = 1
        if draw_check == 0:
            return "draw"
        return "no winner, no draw"
