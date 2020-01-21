import numpy 
import time

#global array
arr = numpy.array( [['7', '8', '9'],
                    ['4', '5', '6'], 
                    ['1', '2', '3']] )

positions = { '1':(2,0), '2':(2,1), '3':(2,2), '4':(1,0), '5':(1,1), '6':(1,2), '7':(0,0), '8':(0,1), '9':(0,2)}

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

def play_round(player, x0):
    while True:
        try:
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
                    print('{} is a Winner!!! Great job!'.format(num))
                    break
                # call the other guy
                print('Next player, please choose your number: ')
                play_round(player, x0)
        except ValueError:
            print('Sorry, you can only choose a number between 1 and 9')
            continue
        else:
            break

def play_game():
    print('Play Tic Tac Toe!')
    x02 = ''
    x01 = ''

    first_player = input('First player, name: ')
    x0 = input('{} do you want to play with x or 0 ?'.format(first_player))
    if x0 == '0':
        x01 = '0'
    elif x0 == 'x' or x0 == 'X':
        x01 = 'x'
    elif x0 != '0' or  x0 != 'x' or x0 != 'X':
        print('What about x ?')
        x01 = 'x'
    current_player = first_player

    second_player = input('Second player, name: ')
    if x01 == 'x':
        print('{} you will have {} '.format(second_player, '0'))
        x02 = '0'
    elif x01 == '0':
        print('{} you will have {} '.format(second_player, 'x'))
        x02 = 'x'
    time.sleep(2)

    draw_board(arr)
    play_round(first_player, x01)
   # while True:
   #     try:
          #  first_num = int(input('{} please choose a number where you want the {} to go: '.format(first_player, x01)))
          #  if first_num > 9 or first_num == 0:
          #      print('The number should be between 1 and 9')
          #      continue 
          #  elif is_cell_taken(arr, first_num, positions):
          #      print('This cell is already filled, please choose another one.')
          #      continue
          #  else:
          #      update_board(arr, first_num, x01)
          #      draw_board(arr)
          #      if win_check(arr):
          #          print('{} is a Winner!!! Great job!'.format(first_num))
          #          break
          #      #call the second guy
          #      second_num = int(input('It is your turn.'))
   #       round_play(first_player, x01)
   #       continue
          #round_play(second_player, x02)
      #  except ValueError:
       #     print('Sorry, you can only choose a number between 1 and 9')
       #     continue
      #  else:
      #      break

#update_board(arr, 5, 'x')
play_game()

