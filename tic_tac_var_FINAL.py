import os
import time
from colorama import Fore, Style

def board():
    os.system("clear")
    print('\n')
    for col_num in range(1, board_size+1):
        if col_num == 1:
            print (Fore.RESET + '      '+ str(col_num), end='   ')
        else:    
            if col_num>9:
                space = '  '
            if col_num <= 9:
                space = '   '
            print (Fore.RESET + str(col_num), end=space)
    print('\n')
    print(Fore.RESET + '    ' + ' ___'*board_size)
    for i in range(0,board_size):
        print(Fore.RESET + (str(i+1)).ljust(2, ' ') + '  |_', end= '')
        n =0
        for s in rows[i]:
            if s == 'X':
                eval("print(Fore."+color1+" + s, end = '')")
            elif s == 'O':
                eval("print(Fore."+color2+" + s, end = '')")
            else:
                print(Fore.RESET + s, end = '')
            if n < board_size-1:
                print(Fore.RESET+'_|_', end= '')
            n = n + 1
        print(Fore.RESET + '_|')
    print('\n')

def fill_field(player):
    if rows[x-1][y-1]== '_':
        if player==player1:
            char='X'
        else:
            char= 'O'
        rows[x-1][y-1]=char
    else:
        print("Sorry, the field is reserved!")
        time.sleep(3)
        return False
    return

def check_win():
    for i in range(0,board_size):
        if rows[i]==['X']*board_size:
            board()
            print(player1," Win!")
            return True
        if rows[i]==['O']*board_size:
            board()
            print(player2," Win!")
            return True
    for i in range(0,board_size):
        s=[]
        for e in range(0,board_size):
            s.append(rows[e][i])
        if s==['X']*board_size:
            board()
            print(player1," Win!")
            return True
        if s==['O']*board_size:
            board()
            print(player2," Win!")
            return True
    s=[]
    for e in range(0,board_size):
        s.append(rows[e][e])
    if s==['X']*board_size:
        board()
        print(player1," Win!")
        return True
    if s==['O']*board_size:
        board()
        print(player2," Win!")
        return True
    s = []
    y_koord = board_size-1
    for i in range(0,board_size):
        s.append(rows[i][y_koord])
        y_koord = y_koord - 1
    if s==['X']*board_size:
        board()
        print(player1," Win!")
        return True
    if s==['O']*board_size:
        board()
        print(player2," Win!")
        return True
    draw_check=0
    for row in rows:
        if '_' in row:
            draw_check=1
    if draw_check==0:
        board()
        print("The game is tie!!")
        return True
    return

def game_board():
    for i in range(0,board_size):
        row=[]
        for i in range(0,board_size):
            row.append('_')
        rows.append(row)
    return

new_game= True
os.system('clear')
while new_game==True:
    C=0
    while C==0:
        print(Style.BRIGHT + "Please, choose the board size between 3 and 30:")
        board_size= input()
        try:
            board_size = int(board_size)
            if board_size in range(3,31):
                C=1
            else:
                print("The size is out of the limit.")
        except ValueError:
            print("Sorry, wrong character! Enter a number between 3 and 30.")
    rows=[]
    player1 = input("Player 1, please enter your name: ")
    C=0
    while C==0:
        print(player1+", please, choose a colour (blue, yellow, red, green, cyan, magenta):")
        color1 = input().upper()
        if color1 in ['BLUE', 'YELLOW', 'RED', 'GREEN', 'CYAN', 'MAGENTA']:
            C=1
        else:
            print("Please, choose a right colour!")
        
    player2 = input("Player 2, please enter your name: ")
    C=0
    while C==0:
        print(player2+", please, choose a colour (blue, yellow, red, green, cyan, magenta):")
        color2 = input().upper()
        if color2 in ['BLUE', 'YELLOW', 'RED', 'GREEN', 'CYAN', 'MAGENTA']:
            C=1
        else:
            print("Please, choose a right colour!")
    win=False
    p=True
    game_board()
    while win==False:
        board()
        if p==True:
            print(player1)
            C=0
            while C==0: 
                x=input("Enter the row number:\n " )
                try:
                    x = int(x)
                    if x in range (1,board_size+1):
                        C=1
                    else:
                        print("The position is out of the board.") 
                except ValueError:
                    print("Sorry, wrong character! Try again!")
            C=0
            while C==0: 
                y=input("Enter the coloumn number:\n " )
                try:
                    y = int(y)
                    if y in range (1,board_size+1):
                        C=1
                    else:
                        print("The position is out of the board.") 
                except ValueError:
                    print("Sorry, wrong character! Try again!")
            p=False
            if fill_field(player1) == False:
                p= True
            if check_win()== True:
                win = True
        else:
            print(player2)
            C=0
            while C==0: 
                x=input("Enter the row number:\n " )
                try:
                    x = int(x)
                    if x in range (1,board_size+1):
                        C=1
                    else:
                        print("The position is out of the board.") 
                except ValueError:
                    print("Sorry, wrong character! Try again!")
            C=0
            while C==0: 
                y=input("Enter the coloumn number:\n " )
                try:
                    y = int(y)
                    if y in range (1,board_size+1):
                        C=1
                    else:
                        print("The position is out of the board.")
                except ValueError:
                    print("Sorry, wrong character! Try again!")
            p=True
            if fill_field(player2) == False:
                p = False
            if check_win()== True:
                win = True
    play_again=input("Do you want Play Again? y/n ")
    if play_again== 'n':
        new_game=False

print(Style.RESET_ALL + '')    
exit()