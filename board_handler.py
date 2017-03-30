from colorama import Fore, Style


def get_board_size():
    return_value = -1
    while True:
        print(Style.BRIGHT + "Please, choose the board size:")
        print("Tic-Tac-Toe (3x3): 3 \nAmoeba (between 5x5 and 30x30): 5-30")
        board_size = input()
        try:
            board_size = int(board_size)
            if board_size in range(3, 31) and board_size != 4:
                return_value = board_size
                break
            else:
                print("The size is out of the limit.")
        except ValueError:
            print("Sorry, wrong character! Enter 3 (Tic-Tac-Toe) or a number from 5 to 30 (Amoeba).")
    return return_value
