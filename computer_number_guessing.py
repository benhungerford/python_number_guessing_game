import random

number = int(input('Enter a number between 1 and 10:'))

guesses = 0

while guesses >= 0 :
    computer_guess = random.randint(1, 10)
    print(str(computer_guess))
    guesses += 1
    if computer_guess != number:
        print('Try again!')
        print(str(computer_guess))
    if computer_guess == number:
        break

print('The computer guessed the number in ' + str(guesses) + ' tries!')
