import os
import time
from colorama import Fore, Style
from game_board import game_board
from board import board
from fill_field import fill_field
from check_win import check_win

new_game = True
os.system('clear')
while new_game == True:
    C = 0
    while C == 0:
        print(Style.BRIGHT + "Please, choose the board size between 3 and 30:")
        board_size = input()
        try:
            board_size = int(board_size)
            if board_size in range(3, 31):
                C = 1
            else:
                print("The size is out of the limit.")
        except ValueError:
            print("Sorry, wrong character! Enter a number between 3 and 30.")
    rows = game_board(board_size)
    player1 = input("Player 1, please enter your name: ")
    C = 0
    while C == 0:
        print(player1 + ", please, choose a colour (blue, yellow, red, green, cyan, magenta):")
        color1 = input().upper()
        if color1 in ['BLUE', 'YELLOW', 'RED', 'GREEN', 'CYAN', 'MAGENTA']:
            C = 1
        else:
            print("Please, choose a right colour!")

    player2 = input("Player 2, please enter your name: ")
    C = 0
    while C == 0:
        print(player2 + ", please, choose a colour (blue, yellow, red, green, cyan, magenta):")
        color2 = input().upper()
        if color2 in ['BLUE', 'YELLOW', 'RED', 'GREEN', 'CYAN', 'MAGENTA']:
            C = 1
        else:
            print("Please, choose a right colour!")
    win = False
    p = True
    while win == False:
        board(rows, board_size, color1, color2)
        if p == True:
            print(player1)
            C = 0
            while C == 0:
                x = input("Enter the row number:\n ")
                try:
                    x = int(x)
                    if x in range(1, board_size + 1):
                        C = 1
                    else:
                        print("The position is out of the board.")
                except ValueError:
                    print("Sorry, wrong character! Try again!")
            C = 0
            while C == 0:
                y = input("Enter the coloumn number:\n ")
                try:
                    y = int(y)
                    if y in range(1, board_size + 1):
                        C = 1
                    else:
                        print("The position is out of the board.")
                except ValueError:
                    print("Sorry, wrong character! Try again!")
            p = False
            if fill_field(rows, x, y, player1, player1) == False:
                p = True
        else:
            print(player2)
            C = 0
            while C == 0:
                x = input("Enter the row number:\n ")
                try:
                    x = int(x)
                    if x in range(1, board_size + 1):
                        C = 1
                    else:
                        print("The position is out of the board.")
                except ValueError:
                    print("Sorry, wrong character! Try again!")
            C = 0
            while C == 0:
                y = input("Enter the coloumn number:\n ")
                try:
                    y = int(y)
                    if y in range(1, board_size + 1):
                        C = 1
                    else:
                        print("The position is out of the board.")
                except ValueError:
                    print("Sorry, wrong character! Try again!")
            p = True
            if fill_field(rows, x, y, player2, player1) == False:
                p = False
        check_win_answer = check_win(rows, board_size)
        if check_win_answer == "player1 wins":
            board(rows, board_size, color1, color2)
            print(player1 + ' wins!')
            win = True
        elif check_win_answer == "player2 wins":
            board(rows, board_size, color1, color2)
            print(player2 + ' wins!')
            win = True
        elif check_win_answer == "draw":
            board(rows, board_size, color1, color2)
            print('The game is tie!!')
            win = True
    play_again = input("Do you want Play Again? y/n ")
    if play_again == 'n':
        new_game = False

print(Style.RESET_ALL + '')
exit()
