# Guess_a_number
# Script of a game that asks the player to guess the number in specific number of attempts.

import random

play = 'Y'

while (play == 'Y' or play == 'y'):
    
    # Asking player for selecting level of game
    print("\n========Guess the number game========")
    print("Levels : ")
    print("1. Basic")
    print("2. Medium")
    print("3. Advance")
    level = int(input("Select level : "))
    
    #Generating random number between a range acording 
    if( level == 1 ):
        print("\nHey, I was thinking of a number between 1 to 20.Can you guess it???")
        # Generating a random number for player to guess.
        secret_number = random.randint(1, 20)
        
    elif( level == 2 ):
        print("\nHey, I was thinking of a number between 1 to 50.Can you guess it???")
        # Generating a random number for player to guess.
        secret_number = random.randint(1, 50)
        
    elif( level == 3):
        print("\nHey, I was thinking of a number between 1 to 100.Can you guess it???")
        # Generating a random number for player to guess.
        secret_number = random.randint(1, 100)
        
    else:
        print("Invalid Input!!!")
    


    for guess_taken in range(1, 6):
        # Taking input from user
        if guess_taken == 1:
            print("Guess the number ")
        elif guess_taken == 5:
            print("\nThis is your last chance.")
        else:
            print("\nGive another try.")
        guess = int(input())

        # Comparing input with secret_number
        if guess > secret_number:
            print("Your guess is too high.")
        elif guess < secret_number:
            print("Your guess is too low.")
        else:
            break  # This condition is for correct guess!

    if guess == secret_number:
        # Executes when player guess the number.
        print("\nGood job! You guessed my number in " +
              str(guess_taken) + " guesses.")
    else:
        # Executes when player fails to guess the number in given chances.
        print("\n\nNope.The number I was thinking of was " +
              str(secret_number) + ".Better luck next time!!!")
    print("\nDo you want to play again?( Y or N )")
    play = input()
    
print("\nThanks for playing!!")
