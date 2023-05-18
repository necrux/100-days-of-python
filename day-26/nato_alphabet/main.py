#!/usr/bin/env python3
import pandas

NATO = 'nato_phonetic_alphabet.csv'

# TODO 1. Create a dictionary in this format:
data = pandas.read_csv(NATO)
alphabet = {row.letter: row.code for (index, row) in data.iterrows()}

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
word = input("Enter a word: ").upper()
phonetic_spelling = [alphabet[letter] for letter in word]
print(phonetic_spelling)
