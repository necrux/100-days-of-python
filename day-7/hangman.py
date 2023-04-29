#!/usr/bin/env python3

import random
import os
import hangman_art
import hangman_words

print(hangman_art.logo)

#word_list = ["aardvark", "baboon", "camel"]
word_list = hangman_words.word_list

# Step 1 
#   TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
# Step 2
#  TODO-1: - Create an empty List called display.
#            For each letter in the chosen_word, add a "_" to 'display'.
#            So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.
# Step 4
#  TODO-1: - Create a variable called 'lives' to keep track of the number of lives left. 
#            Set 'lives' to equal 6.
# Step 5
#  TODO-1: - Update the word list to use the 'word_list' from hangman_words.py
#            Delete this line: word_list = ["ardvark", "baboon", "camel"]
#  TODO-2: - Import the stages from hangman_art.py and make this error go away.
#  TODO-3: - Import the logo from hangman_art.py and print it at the start of the game.

# My Original Solution
chosen_word = word_list[random.randint(0, len(word_list) - 1)]
# Preferred Solution
chosen_word = random.choice(word_list)

# Testing code
print(f'Pssst, the solution is {chosen_word}.')

display = []
for letter in chosen_word:
    display += "_"

lives = 6

# Step 1 
#  TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
# Step 2
#  TODO-2: - Loop through each position in the chosen_word;
#            If the letter at that position matches 'guess' then reveal that letter in the display at that position.
#            e.g. If the user guessed "p" and the chosen word was "apple", then display should be ["_", "p", "p", "_", "_"].

# Moving this logic down as of 'Step 3'.
#guess = input("Guess a letter: ").lower()
#
#count = 0
#for letter in chosen_word:
#    if letter == guess:
#        display[count] = letter 
#    count += 1

# Step 1 
#  TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
# Step 2
#  TODO-3: - Print 'display' and you should see the guessed letter in the correct position and every other letter replace with "_".
#            Hint - Don't worry about getting the user to guess the next letter. We'll tackle that in step 3.
# Step 3
#  TODO-1: - Use a while loop to let the user guess again. The loop should only stop once the user has guessed all the letters in the chosen_word and 'display' has no more blanks ("_"). Then you can tell the user they've won.
# Step 4
#  TODO-2: - If guess is not a letter in the chosen_word,
#            Then reduce 'lives' by 1. 
#            If lives goes down to 0 then the game should stop and it should print "You lose."
#  TODO-3: - print the ASCII art from 'stages' that corresponds to the current number of 'lives' the user has remaining.
# Step 5
#  TODO-4: - If the user has entered a letter they've already guessed, print the letter and let them know.
#  TODO-5: - If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.

guesses = []

while "_" in display:
    guess = input("\nGuess a letter: ").lower()
    os.system("clear")
    
    if guess in guesses:
        print(f"You've already guessed {guess}.")
        print(hangman_art.stages[lives])
    elif guess in chosen_word:
        print("Correct!")
        count = 0
        for letter in chosen_word:
            if letter == guess:
                display[count] = letter
            count += 1
        print(*display, sep = " ")
    else:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        print(hangman_art.stages[lives])
        if lives == 0:
            print("You lose.")
            exit(0)
    guesses += guess
print("You Win!")
