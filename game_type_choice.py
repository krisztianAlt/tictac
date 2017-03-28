from colorama import Fore, Style


def get_game_type_choice():

    while True:
        print(Style.BRIGHT + "Choose with whom you'd like to play? human or computer")
        game_type = input()
        try:
            if game_type == "c":
                return True

            if game_type == "h":
                return False
        except ValueError:
            print("Sorry, wrong character! Enter a h or c")
