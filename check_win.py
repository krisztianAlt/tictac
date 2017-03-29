from board import board


def check_win(rows, board_size):
    if (board_size == 3) or (board_size == 4):
        for i in range(0, board_size):
            if rows[i] == ['X'] * board_size:
                return "player1 wins"
            if rows[i] == ['O'] * board_size:
                return "player2 wins"
        for i in range(0, board_size):
            s = []
            for e in range(0, board_size):
                s.append(rows[e][i])
            if s == ['X'] * board_size:
                return "player1 wins"
            if s == ['O'] * board_size:
                return "player2 wins"
        s = []
        for e in range(0, board_size):
            s.append(rows[e][e])
        if s == ['X'] * board_size:
            return "player1 wins"
        if s == ['O'] * board_size:
            return "player2 wins"
        s = []
        y_koord = board_size - 1
        for i in range(0, board_size):
            s.append(rows[i][y_koord])
            y_koord = y_koord - 1
        if s == ['X'] * board_size:
            return "player1 wins"
        if s == ['O'] * board_size:
            return "player2 wins"
        draw_check = 0
        for row in rows:
            if '_' in row:
                draw_check = 1
        if draw_check == 0:
            return "draw"
        return "no winner, no draw"
    elif board_size > 4:
        for i in range(0, board_size):
            start_pos = 0
            row = rows[i]
            for _ in range(0, (board_size-4)):
                if ''.join(row[start_pos:(start_pos+5)]) == 'XXXXX':
                    return "player1 wins"
                if ''.join(row[start_pos:(start_pos+5)]) == 'OOOOO':
                    return "player2 wins"
                start_pos += 1
        for i in range(0, board_size):
            start_pos = 0
            col = []
            for e in range(0, board_size):
                col.append(rows[e][i])
            for e in range(0, board_size-4):
                if ''.join(col[start_pos:(start_pos+5)]) == 'XXXXX':
                    return "player1 wins"
                if ''.join(col[start_pos:(start_pos+5)]) == 'OOOOO':
                    return "player2 wins"
                start_pos += 1
        diagonal1 = []
        for row_start in range(0, board_size-4):
            new_diag = []
            y = 0
            for e in range(row_start, board_size):
                new_diag.append(rows[e][y])
                y += 1
            diagonal1.append(new_diag)
        for col_start in range(1, board_size-4):
            new_diag = []
            x = 0
            for e in range(col_start, board_size):
                new_diag.append(rows[x][e])
                x += 1
            diagonal1.append(new_diag)
        for diag in diagonal1:
            start_pos = 0
            for e in range(0, len(diag)-4):
                if ''.join(diag[start_pos:(start_pos+5)]) == 'XXXXX':
                    return "player1 wins"
                if ''.join(diag[start_pos:(start_pos+5)]) == 'OOOOO':
                    return "player2 wins"
                start_pos += 1

        diagonal2 = []
        for row_start in range(0, board_size-4):
            new_diag = []
            y = board_size - 1
            for e in range(row_start, board_size):
                new_diag.append(rows[e][y])
                y -= 1
            diagonal2.append(new_diag)
        for col_start in range(board_size-2, 3, -1):
            new_diag = []
            x = 0
            for e in range(col_start, -1, -1):
                new_diag.append(rows[x][e])
                x += 1
            diagonal2.append(new_diag)
        for diag in diagonal2:
            start_pos = 0 
            for e in range(0, board_size-4):
                if ''.join(diag[start_pos:(start_pos+5)]) == 'XXXXX':
                    return "player1 wins"
                if ''.join(diag[start_pos:(start_pos+5)]) == 'OOOOO':
                    return "player2 wins"
                start_pos += 1
        draw_check = 0
        for row in rows:
            if '_' in row:
                draw_check = 1
        if draw_check == 0:
            return "draw"
        return "no winner, no draw"
