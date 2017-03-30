from board import board
import random
import time


def get_computer_coordinates(rows, board_size, opponent_char):
    if (board_size == 3) or (board_size == 4):
        if opponent_char == 'O':
            for row_index in range(0, board_size):
                if rows[row_index] == ['O', '_', 'O']:
                    return row_index+1, 2
                if rows[row_index] == ['O', 'O', '_']:
                    return row_index+1, 3
                if rows[row_index] == ['_', 'O', 'O']:
                    return row_index+1, 1
            
            for row_item in range(0, board_size):
                coloumn = []
                for row_index in range(0, board_size):
                    coloumn.append(rows[row_index][row_item])
                if coloumn == ['O', '_', 'O']:
                    return 2, row_item+1
                if coloumn == ['O', 'O', '_']:
                    return 3, row_item+1
                if coloumn == ['_', 'O', 'O']:
                    return 1, row_item+1
            
            diagonal_left = []
            for index in range(0, board_size):
                diagonal_left.append(rows[index][index])
            if diagonal_left == ['O', '_', 'O']:
                    return 2, 2
            if diagonal_left == ['O', 'O', '_']:
                    return 3, 3
            if diagonal_left == ['_', 'O', 'O']:
                    return 1, 1
        
            diagonal_right = []
            y_koord = board_size - 1
            for row_index in range(0, board_size):
                diagonal_right.append(rows[row_index][y_koord])
                y_koord = y_koord - 1
            if diagonal_right == ['O', '_', 'O']:
                    return 2, 2
            if diagonal_right == ['O', 'O', '_']:
                    return 3, 1
            if diagonal_right == ['_', 'O', 'O']:
                    return 1, 3

        elif opponent_char == 'X':
            for row_index in range(0, board_size):
                if rows[row_index] == ['X', '_', 'X']:
                    return row_index+1, 2
                if rows[row_index] == ['X', 'X', '_']:
                    return row_index+1, 3
                if rows[row_index] == ['_', 'X', 'X']:
                    return row_index+1, 1
                
            for row_item in range(0, board_size):
                coloumn = []
                for row_index in range(0, board_size):
                    coloumn.append(rows[row_index][row_item])
                if coloumn == ['X', '_', 'X']:
                    return 2, row_item+1
                if coloumn == ['X', 'X', '_']:
                    return 3, row_item+1
                if coloumn == ['_', 'X', 'X']:
                    return 1, row_item+1
                
            diagonal_left = []
            for index in range(0, board_size):
                diagonal_left.append(rows[index][index])
            if diagonal_left == ['X', '_', 'X']:
                    return 2, 2
            if diagonal_left == ['X', 'X', '_']:
                    return 3, 3
            if diagonal_left == ['_', 'X', 'X']:
                    return 1, 1
            
            diagonal_right = []
            y_koord = board_size - 1
            for row_index in range(0, board_size):
                diagonal_right.append(rows[row_index][y_koord])
                y_koord = y_koord - 1
            if diagonal_right == ['X', '_', 'X']:
                    return 2, 2
            if diagonal_right == ['X', 'X', '_']:
                    return 3, 1
            if diagonal_right == ['_', 'X', 'X']:
                    return 1, 3

        for row_index in range(0, board_size):
            if (
                rows[row_index] == ['X', '_', 'X'] or rows[row_index] == ['O', '_', 'O'] or
                rows[row_index] == ['X', '_', 'O'] or rows[row_index] == ['O', '_', 'X']
               ):
                return row_index+1, 2
            if rows[row_index] == ['X', 'X', '_'] or rows[row_index] == ['O', 'O', '_']:
                return row_index+1, 3
            if rows[row_index] == ['_', 'X', 'X'] or rows[row_index] == ['_', 'O', 'O']:
                return row_index+1, 1
            
        for row_item in range(0, board_size):
            coloumn = []
            for row_index in range(0, board_size):
                coloumn.append(rows[row_index][row_item])
            if (
                coloumn == ['X', '_', 'X'] or coloumn == ['O', '_', 'O'] or
                rows[row_index] == ['X', '_', 'O'] or rows[row_index] == ['O', '_', 'X']
               ):
                return 2, row_item+1
            if coloumn == ['X', 'X', '_'] or coloumn == ['O', 'O', '_']:
                return 3, row_item+1
            if coloumn == ['_', 'X', 'X'] or coloumn == ['_', 'O', 'O']:
                return 1, row_item+1
            
        diagonal_left = []
        for index in range(0, board_size):
            diagonal_left.append(rows[index][index])
        if (
            diagonal_left == ['X', '_', 'X'] or diagonal_left == ['O', '_', 'O'] or
            rows[row_index] == ['X', '_', 'O'] or rows[row_index] == ['O', '_', 'X']
           ):
                return 2, 2
        if diagonal_left == ['X', 'X', '_'] or diagonal_left == ['O', 'O', '_']:
                return 3, 3
        if diagonal_left == ['_', 'X', 'X'] or diagonal_left == ['_', 'O', 'O']:
                return 1, 1
        
        diagonal_right = []
        y_koord = board_size - 1
        for row_index in range(0, board_size):
            diagonal_right.append(rows[row_index][y_koord])
            y_koord = y_koord - 1
        if (
            diagonal_right == ['X', '_', 'X'] or diagonal_right == ['O', '_', 'O'] or
            rows[row_index] == ['X', '_', 'O'] or rows[row_index] == ['O', '_', 'X']
           ):
                return 2, 2
        if diagonal_right == ['X', 'X', '_'] or diagonal_right == ['O', 'O', '_']:
                return 3, 1
        if diagonal_right == ['_', 'X', 'X'] or diagonal_right == ['_', 'O', 'O']:
                return 1, 3
        
        count_X = 0
        count_O = 0
        for row in rows:
            for element in row:
                if element == 'X':
                    count_X += 1
                if element == 'O':
                    count_O += 1
        if (count_X == 1) or (count_O == 1):
            x = random.randrange(0, board_size)
            y = random.randrange(0, board_size)
            return x+1, y+1

        empty_board_check = 0
        for row in rows:
            if ('X' in row) or ('O' in row):
                empty_board_check = 1
        if empty_board_check == 0:
            return 2, 2
        
        empty_fields = []
        for row_index in range(0, len(rows)):
            row = rows[row_index]
            for index in range(0, len(row)):
                if row[index] == '_':
                    empty_fields.append((row_index, index))
        tuple_index = random.randrange(0, len(empty_fields))
        print(tuple_index)
        x = empty_fields[tuple_index][0] + 1
        y = empty_fields[tuple_index][1] + 1
        print(x, y)
        time.sleep(2)
        return x, y
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
