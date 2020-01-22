import numpy 
import time
import random

# global array - board
arr = numpy.array( [['7', '8', '9'],
                    ['4', '5', '6'], 
                    ['1', '2', '3']] )

# global dictionary for position on board
positions = { '1':(2,0), '2':(2,1), '3':(2,2), '4':(1,0), '5':(1,1), '6':(1,2), '7':(0,0), '8':(0,1), '9':(0,2)}

#global players
first_player = ''
second_player = ''
x01 = ''
x02 = ''

def get_position(positions, num_str):
    for key, item in positions.items():
        if key == num_str:
            return item

def reset_board(arr):
    arr[2,0] = 1
    arr[2,1] = 2
    arr[2,2] = 3
    arr[1,0] = 4
    arr[1,1] = 5
    arr[1,2] = 6
    arr[0,0] = 7
    arr[0,1] = 8
    arr[0,2] = 9

# draw the board
def draw_board(arr):
    for i in range(0,3):
        print(' {} | {} | {}'.format(arr[i, 0], arr[i, 1], arr[i, 2]))
        print('--- --- ---')

# update the board based on user's choice
def update_board(arr, num, x_or_0):
    if num == 9:
       arr[0,2] = x_or_0
    elif num == 8:
        arr[0,1] = x_or_0
    elif num == 7:
        arr[0,0] = x_or_0
    elif num == 6:
        arr[1,2] = x_or_0
    elif num == 5:
        arr[1,1] = x_or_0
    elif num == 4:
        arr[1,0] = x_or_0
    elif num == 3:
        arr[2,2] = x_or_0
    elif num == 2:
        arr[2,1] = x_or_0
    elif num == 1:
        arr[2,0] = x_or_0
    else:
        pass

# return True if there is a winner
def win_check(arr):
    diagonal1 = tuple((arr[0,0], arr[1,1], arr[2,2]))
    diagonal2 = tuple((arr[0,2], arr[1,1], arr[2,0]))
    column = tuple()
    row = tuple()
    is_winner = False

    for c in range(0,3):
        row = (arr[c,0], arr[c,1], arr[c,2])
        column = (arr[0,c], arr[1,c], arr[2,c])
    
        if (cmpT(row[0], row[1], row[2]) 
        or cmpT(column[0], column[1], column[2]) 
        or cmpT(diagonal1[0], diagonal1[1], diagonal1[2]) 
        or cmpT(diagonal2[0], diagonal2[1], diagonal2[2])):
            is_winer = True
            return is_winer
    return is_winner

# compares if equals
def cmpT(t1, t2, t3):
    return t1 == t2 == t3

# checks if the cell on the board is taken already
def is_cell_taken(arr, num, positions):
    for i in range(0,10):
        cell = get_position(positions, str(num))
        return arr[cell[0], cell[1]] == 'x' or arr[cell[0], cell[1]] == '0'

# maybe find a different way to solve this
# checks to see if board is full
def is_board_full(arr):
    str_list = list()
    for i in range(0,3):
       for m in arr[:, i]:
           str_list.append(m)
           
    for i in range(1,10):
        str_i = str(i)
        if str_i in str_list:
            break
        else:
            return True

def play_round(player, x0):
    while True:
        try:
            if is_board_full(arr):
                print('Game over! No winners!')
                break
            num = int(input('{} please choose a number where you want the {} to go: '.format(player, x0)))
            if num > 9 or num == 0:
                print('The number should be between 1 and 9')
                continue 
            elif is_cell_taken(arr, num, positions):
                print('This cell is already filled, please choose another one.')
                continue
            else:
                update_board(arr, num, x0)
                draw_board(arr)
                if win_check(arr):
                    print('{} is a Winner!!! Great job!'.format(player))
                    return True
                    break
        except ValueError:
            print('Sorry, you can only choose a number between 1 and 9')
            continue
        else:
            break

def play_game(first_player, second_player, x01, x02):
    print('Play Tic Tac Toe!')

# settup the players - this ca be simplified and put in a separate function
    first_player = input('First player, name: ')
    if(first_player == ''):
        first_player = 'Bob'
        print('I will call you Bob!')
    x0 = input('{} do you want to play with x or 0 ?'.format(first_player))
    if x0 == '0':
        x01 = '0'
    elif x0 == 'x' or x0 == 'X':
        x01 = 'x'
    elif x0 != '0' or  x0 != 'x' or x0 != 'X':
        print('What about x ?')
        x01 = 'x'

    second_player = input('Second player, name: ')
    if(second_player == ''):
        second_player == 'Mikey'
        print('I will call you Mikey!')
    if x01 == 'x':
        print('{} you will have {} '.format(second_player, '0'))
        x02 = '0'
    elif x01 == '0':
        print('{} you will have {} '.format(second_player, 'x'))
        x02 = 'x'
    time.sleep(1)
    
    reset_board(arr)
    draw_board(arr) 
    
    isFirstWinner = play_round(first_player, x01)
    isSecondWinner =  play_round(second_player, x02)
    while True: 
        isFirstWinner = play_round(first_player, x01)
        if isFirstWinner or isSecondWinner or is_board_full(arr):
            play_again = input('Do you want to play again? Y | N: ').lower()
            if play_again == 'y':
                play_game(first_player, second_player, x01, x02)
            elif play_again == 'n':
                break

        isSecondWinner = play_round(second_player, x02)
        if isFirstWinner or isSecondWinner or is_board_full(arr): 
            play_again = input('Do you want to play again? Y | N: ').lower()
            if play_again == 'y':
                play_game(first_player, second_player, x01, x02)
            elif play_again == 'n':
                break


play_game(first_player, second_player, x01, x02)

