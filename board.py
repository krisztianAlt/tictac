import os
from colorama import Fore, Style


def board(rows, board_size, color1, color2):
    os.system("clear")
    print('\n')
    for col_num in range(1, board_size + 1):
        if col_num == 1:
            print (Fore.RESET + '      ' + str(col_num), end='   ')
        else:
            if col_num > 9:
                space = '  '
            if col_num <= 9:
                space = '   '
            print (Fore.RESET + str(col_num), end=space)
    print('\n')
    print(Fore.RESET + '    ' + ' ___' * board_size)
    for i in range(0, board_size):
        print(Fore.RESET + (str(i + 1)).ljust(2, ' ') + '  |_', end='')
        n = 0
        for s in rows[i]:
            if s == 'X':
                eval("print(Fore." + color1 + " + s, end = '')")
            elif s == 'O':
                eval("print(Fore." + color2 + " + s, end = '')")
            else:
                print(Fore.RESET + s, end='')
            if n < board_size - 1:
                print(Fore.RESET + '_|_', end='')
            n = n + 1
        print(Fore.RESET + '_|')
    print('\n')
