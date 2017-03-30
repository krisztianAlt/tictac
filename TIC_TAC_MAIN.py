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
from computer import *


new_game = True
os.system('clear')

while new_game == True:
    human_vs_computer = False
    board_size = get_board_size()
    rows = game_board(board_size)
    computer_first = True
    two_human = True
    if board_size == 3:
        human_vs_computer = get_game_type_choice()
        if human_vs_computer == True:
            print("Who should be the first player? If Computer/1, if Human/anything else")
            game_order = input()
            two_human = False
            if game_order == "1":
                print("Computer is the first Player")
                player1 = "Computer"
                player2 = get_player_name("Player 2")
                color2 = get_player_color()
                color1 = get_computer_color(color2)
                opponent_char = 'O'
            else:
                print("Computer is the second Player")
                player1 = get_player_name("Player 1")
                color1 = get_player_color()
                player2 = "Computer"
                color2 = get_computer_color(color1)
                computer_first = False
                opponent_char = 'X'

    if two_human == True:
        player1 = get_player_name("Player 1")
        color1 = get_player_color()
        player2 = get_player_name("Player 2")
        color2 = get_player_color()

    win = False
    player_turn = True
    while win == False:
        if human_vs_computer == True:
            board(rows, board_size, color1, color2)
            if computer_first == True:
                if player_turn == True:
                    print(player1)
                    x, y = get_computer_coordinates(rows, board_size, opponent_char)
                    player_turn = False
                    if fill_field(rows, x, y, player1, player1) == False:
                        print("Computer is thinking...")
                        time.sleep(2)
                        player_turn = True
                else:
                    print(player2)
                    x = get_x(board_size)
                    y = get_y(board_size)
                    player_turn = True
                    if fill_field(rows, x, y, player2, player1) == False:
                        print("Sorry the field is reserved!")
                        time.sleep(2)
                        player_turn = False
            else:
                if player_turn == True:
                    print(player1)
                    x = get_x(board_size)
                    y = get_y(board_size)
                    player_turn = False
                    if fill_field(rows, x, y, player1, player1) == False:
                        print("Sorry the field is reserved!")
                        time.sleep(2)
                        player_turn = True

                else:
                    print(player2)
                    x, y = get_computer_coordinates(rows, board_size, opponent_char)
                    player_turn = True
                    if fill_field(rows, x, y, player2, player1) == False:
                        print("Computer is thinking...")
                        time.sleep(2)
                        player_turn = False

        else:
            board(rows, board_size, color1, color2)
            if player_turn == True:
                print(player1)
                x = get_x(board_size)
                y = get_y(board_size)
                player_turn = False
                if fill_field(rows, x, y, player1, player1) == False:
                    print("Sorry the field is reserved!")
                    time.sleep(2)
                    player_turn = True
            else:
                print(player2)
                x = get_x(board_size)
                y = get_y(board_size)
                player_turn = True
                if fill_field(rows, x, y, player2, player1) == False:
                    print("Sorry the field is reserved!")
                    time.sleep(2)
                    player_turn = False

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
        print("Starting new game...")


print(Style.RESET_ALL + '')
exit()
