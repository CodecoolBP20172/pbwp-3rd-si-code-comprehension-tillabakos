import random

#  Geassing game. Runs until input maches the number to be guessed or gesses reach max guesses defined.    

guessesTaken = 0  # value assigned to variable

print('Hello! What is your name?')  # print string to console
myName = input()  # assigne consol input to variable

number = random.randint(1, 20)  # assigne value to variable randomely from range 1 to 20
print('Well, ' + myName + ', I am thinking of a number between 1 and 20.')  # print string and value of variable to console

while guessesTaken < 6:  # loop until condition is True
    print('Take a guess.')  # print string to console
    guess = input()  # assigne console input to variable
    guess = int(guess)  # change type of variable to integer

    guessesTaken += 1  # add one to variable in every loop

    if guess < number:  # check if condition is True
        print('Your guess is too low.')  # print string to console

    if guess > number:  # check if condition is True
        print('Your guess is too high.')  # print string to console

    if guess == number:  # check if condition is True
        break  # stop the loop an d go to the next line

if guess == number:  # check if condition is True
    guessesTaken = str(guessesTaken)  # change the type of varianble to string
    print('Good job, ' + myName + '! You guessed my number in ' + guessesTaken + ' guesses!')  # print strings combined with variables to console

if guess != number:  # check if condition is True
    number = str(number)  # change the type of varianble to string
    print('Nope. The number I was thinking of was ' + number)  # print string and variable to console
