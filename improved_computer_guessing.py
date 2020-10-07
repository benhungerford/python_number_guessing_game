def computer_guess(number):
    lower = 1
    higher = 100
    guess = 50
    guesses = 0
    while guesses < 6:
        guess = (lower+higher)//2
        print("The computer guesses", guess)
        guesses += 1
        if guess > number:
            higher = guess
        elif guess < number:
            lower = guess + 1
        elif guess == number:
            print('The computer guessed', guess, 'correctly!')
            break

        if guesses > 5:
            print('The computer did not guess the number.')





def main():
    number = int(input("Enter a number: "))
    if number < 1 or number > 100:
        print("Must be in range [1, 100]")
    else:
        computer_guess(number)


main()
