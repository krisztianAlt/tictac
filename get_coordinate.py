def get_x(board_size):
    return_value = -1
    while True:
        x = input("Enter the row number:\n ")
        try:
            x = int(x)
            if x in range(1, board_size + 1):
                return_value = x
                break
            else:
                print("The position is out of the board.")
        except ValueError:
            print("Sorry, wrong character! Try again!")
    return return_value


def get_y(board_size):
    return_value = -1
    while True:
        y = input("Enter the coloumn number:\n ")
        try:
            y = int(y)
            if y in range(1, board_size + 1):
                return_value = y
                break
            else:
                print("The position is out of the board.")
        except ValueError:
            print("Sorry, wrong character! Try again!")
    return return_value
