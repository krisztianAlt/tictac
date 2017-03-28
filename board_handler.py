from colorama import Fore, Style


def get_board_size():

    return_value = -1
    while True:
        print(Style.BRIGHT + "Please, choose the board size between 3 and 30:")
        board_size = input()
        try:
            board_size = int(board_size)
            if board_size in range(3, 31):
                return_value = board_size
                break
            else:
                print("The size is out of the limit.")
        except ValueError:
            print("Sorry, wrong character! Enter a number between 3 and 30.")
    return return_value
