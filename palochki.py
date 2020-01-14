### excercise 2 v1.3 ###
### TODO: make cases for 2 and 1 sticks left; handle exception for non integers ###

# defining core vars
players = [] 
player_name = None
default_player_number = 0
turn = 0

# announcements
print('Welcome to stick game!\n')
print('\nChoose names for players.\nYou can leave it blank for default name.\n')

# ask for names
stick = int(input('Choose, how many sticks will be in the game: '))

while len(players) != 2: # because only 2 players
    player_name = input('Enter your Name: ')
    if not player_name: # to define default names
        default_player_number += 1
        players.append("player"+str(default_player_number))
    else:
        players.append(player_name) # pass name to list
        
# core logic
while stick > 0:
    stick_taken = int(input(f'{players[turn]}, how many sticks you wanna take? ')) # ask for sticks
    if stick_taken > 3 or stick_taken < 1: # allow to take only certain amount of sticks
        print(f'{players[turn]}, you took {stick_taken} sticks, and only 1, 2 or 3 stick are allowed to take.')
        continue
    if stick > 0: # normal case
        stick = stick - stick_taken
        print(f'{players[turn]} took {stick_taken} sticks, and {stick} are left')
    if stick <= 0: # lose case
        print(f'{players[turn]} has lost!');
        break;
        
    # switch turn
    if turn == 0:
        turn = 1
    else:
        turn = 0