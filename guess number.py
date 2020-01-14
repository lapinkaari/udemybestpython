### excercise in python v 1.2 ###

# importing modules
import random

computer_number = random.randint(1, 50) # get random integer number

tries = 6 # set number of tries

count = 0 # counter initialisation

# welcome message
print('GAME: Try to guess the number :)')

# main game logic
while count < tries:
    try:
        human_number = input('Enter integer number from 1 to 50: ') # get the number from human
        human_number = int(human_number) # making inpunt an integer
        count += 1 # counter incrementation
        if human_number == computer_number: # win case
            print(f"You've guessed the number in {count} tries!")
            break;
        elif human_number != computer_number and count == tries: # gameover case
            print(f"You are out of tries, game over! The number was {computer_number}")
        elif human_number > 50 or human_number < 1: # wrong number case
            print(f"The number you've entered is not in range, dumbass! You have", tries-count, "more tries")
        elif human_number < computer_number: # less case
            print(f"The number you've entered is less than guessed, you have", tries-count, "more tries")
        elif human_number > computer_number: # more case
            print(f"The number you've entered is greater than guessed, you have", tries-count, "more tries")
    # handlig exception if user input is not a number
    except:
        count += 1 # counter incrementation
        if count == tries: # gameover case
            print(f"You're hopeless...")
            break;
        print(f"Your inpunt is not a number! You have", tries-count, "more tries")