import random


def get_player_name(player):
    player = str(player)
    player_name = input(player + ", please enter your name: ")
    return player_name


def get_player_color():
    while True:
        print("Please, choose a colour(blue, yellow, red, green, cyan, magenta): ")
        color_name = input().upper()
        if color_name in ['BLUE', 'YELLOW', 'RED', 'GREEN', 'CYAN', 'MAGENTA']:
            return_value = color_name
            break
        else:
            print("Please, choose a right colour!")
    return return_value


def get_computer_color(player_color):
    return_value = player_color
    color_name = ['BLUE', 'YELLOW', 'RED', 'GREEN', 'CYAN', 'MAGENTA']
    while player_color == return_value:
        return_value = random.choice(color_name)
    return return_value


def get_computer_name():
    computer_name = 'Computer'
    return computer_name
