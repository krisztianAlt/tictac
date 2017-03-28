import os
import time
from colorama import Fore, Style
from game_board import game_board
from board import board
from fill_field import fill_field
from check_win import check_win
from board_handler import get_board_size
from game_type_choice import get_game_type_choice
from get_coordinate import *
from get_player_data import *


new_game = True
os.system('clear')
game_type_choice = False
while new_game == True:
    game_type_choice = get_game_type_choice()
    if game_type_choice == True:
        print('computer game ready')

    board_size = get_board_size()
    rows = game_board(board_size)

    player1 = get_player_name("Player 1")
    color1 = get_player_color()
    player2 = get_player_name("Player 2")
    color2 = get_player_color()

    win = False
    p = True
    while win == False:
        board(rows, board_size, color1, color2)
        if p == True:
            print(player1)
            x = get_x(board_size)
            y = get_y(board_size)
            p = False
            if fill_field(rows, x, y, player1, player1) == False:
                p = True
        else:
            print(player2)
            x = get_x(board_size)
            y = get_y(board_size)
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
    else:
        new_game = True
        print("starting new game...")


print(Style.RESET_ALL + '')
exit()
