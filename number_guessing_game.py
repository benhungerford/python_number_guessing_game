import random

number = random.randint(1, 50)

name  = input("Hello, I have a guessing game for you! What is your name?:")

guesses = 0

print('Alright, ' + name + ', I am thinking of a number between 1 and 50. Can you guess it in 5 tries?')

while guesses < 5 :
    guess = int(input())
    guesses += 1
    if guess < number:
        print('Your guess is too low')
    if guess > number:
        print('Your guess is too high')
    if guess == number:
        break

if guess == number:
    print('Correct! You guessed the number in ' + str(guesses) + ' tries!')
else:
    print('You did not guess the number, The number was ' + str(number))
