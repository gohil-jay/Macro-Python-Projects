# Guess_a_number
#Script of a game that asks the player to guess the number in specific number of attempts.

import random

play = 'Y'
while play='Y':
    print("Hey, I was thinking of a number between 1 to 20.Can you guess it???") 
    secret_number = random.randint(1, 20) #Generating a random number for player to guess.


    for guess_taken in range(1, 7):
        #Taking input from user
        if guess_taken == 1:
            print("Guess the number ")
        elif guess_taken == 6:
            print("This is your last chance.")
        else:
            print("Give another try.")
        guess = int(input())

        #Comparing input with secret_number
        if guess > secret_number:
            print("Your guess is too high.")
        elif guess < secret_number:
            print("Your guess is too low.")
        else:
            break #This condition is for correct guess! 

    if guess == secret_number:
        print("Good job! You guessed my number in " + str(guess_taken) + " guesses.") #Executes when player guess the number.
    else:
        print("Nope.The number I was thinking of was " + str(secret_number) + ".Better luck next time!!!") #Executes when player fails to guess the number in given chances.
    print("Do you want to play again? Y or N")
    repeat = input()
