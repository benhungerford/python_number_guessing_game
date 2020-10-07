import random

with open ('/usr/share/dict/words') as infile:
    words = infile.read().splitlines()

def start_game():
    # generating a random word from the words list // .lower() makes all the words lower case
    random_word = random.choice(words).lower()

    char_list = list(random_word) # ['a', 'p', 'p', 'l', 'e']
    # displays the empty spaces the length of the random_word
    display_list = ['_'] * len(random_word) # ['_', '_', '_', '_', '_']

    remaining_guesses = 10
    guesses_made = []

    #For development purposes only
    print(f'Your random word is {random_word}')
    print(f'There are {len(random_word)} letters in your word.')

    while remaining_guesses > 0:
        # .lower keeps letter lowercase even if user has caps lock on
        guess = input('Guess a letter: ').lower()

        if guess in guesses_made:
            print("Uh oh! You've guessed that letter already. Guess again.")
        else:
            # puts the guess into the guesses_made list to be checked by the first if statement
            guesses _made.append(guess)

            # takes the guess and iterates over the word and then takes the same index and updates the display_list with the matching letter
            if guess in char_list:
                for index, char in enumerate(char_list):
                    if char == guess:
                        display_list[index] = guess
                if '_' not in display_list:
                    print("Congratulations! You're a winner!")
                    break
                else:
                    print("Great job! You've guessed a letter.")
                    print(''.join(display_list))
            else:
                remaining_guesses -= 1
                if remaining_guesses == 0:
                    print('You are a LOSER')
                else:
                    if remaining_guesses == 1
                        guess_text = 'guess'
                    else:
                        guess_text == 'guesses'
                        remaining_guesses == 0
                    print(f"That's not one of the letters. You have {remaining_guesses} left")
                    print(''.join(display_list))



# import random
# #list of words
# with open ('/usr/share/dict/words') as infile:
#     words = infile.read()
#     #ask Name
# name=input("Hello! What is your name? ")
# print(f"Hi {name} , Let's start the game")
#
# print("\nYou have 10 attempts to guess the word correctly.")
# #list to store wrong guessed_letters
# wrong_list = []
# #generate random word
# original_word = random.choice(words)
# print(original_word)
# print(f"The word I'm thinking of is {len(original_word)} letters long. ")
# #create an empty list
# guessed_word = []
# for i in range(len(original_word)):
#     guessed_word.append("_")
# print(*([i for i in guessed_word]))
# c = 8
# while(c):
#     c=c-1
#     #take input from user
#     guessed_letter = input("Guess a letter: ")
#     #check if guessed_letter is an alphabet
#     if not guessed_letter.isalpha():
#         print('Guess only a letter: ')
#     #check if guessed letter length is one or not
#     elif(len(guessed_letter)>1):
#         print('Guess only one letter: ')
#     #check that letter chosen by user is already guessed or not
#     elif(guessed_letter in wrong_list):
#         print('You have Already guessed this letter')
#     #check if guessed_letter is matches with original_word
#     if guessed_letter in original_word:
#         for i in range(len(original_word)):
#             if original_word[i] == guessed_letter:
#                 guessed_word[i] = original_word[i]
#     else:
#         """if guessed_letter is not in original_word
#            prompt user for wrong chosen letter"""
#         print("You guessed a wrong letter.")
#         wrong_list.append(guessed_letter)
#     guess_word = [i for i in guessed_word]
#     guess_word = "".join(guess_word)
#     if original_word == guess_word :
#         print(f'Yay! You win! The word was {original_word}')
#         exit(0)
#     #print the guessed word
#     print(*([i for i in guessed_word]))
#     #prompt user showing number of attempts left to win
#     print(f"You have {c} attempts left")
#     if c == 0:
#         if  original_word != guessed_word  :
#             print(f"You lost the game ,The word was {original_word}")
#             exit(0)

# words = /usr/share/dict/words

# import random
#
# name = input("What is your name? ")
#
# print("Good Luck ! ", name)
#
# words = open("/usr/share/dict/words", "r")
# word = words.read(random.choice(words))
#
# # word = random.choice(words)
#
# print("Guess the characters")
#
# guesses = ''
# turns = 12
#
# while turns > 0:
#
# 	failed = 0
#
# 	for char in word:
# 		if char in guesses:
# 			print(char)
# 		else:
# 			print("_")
# 			failed += 1
#
# 	if failed == 0:
# 		print("You Win")
# 		print("The word is: ", word)
# 		break
#
# 	guess = input("guess a character:")
#
# 	guesses += guess
#
# 	if guess not in word:
# 		turns -= 1
# 		print("Wrong")
# 		print("You have", + turns, 'more guesses')
#
# 		if turns == 0:
# 			print("You Lose")
