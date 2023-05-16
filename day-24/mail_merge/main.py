#!/usr/bin/env python3
# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

INVITEES = 'Input/Names/invited_names.txt'
TEMPLATE = 'Input/Letters/starting_letter.txt'
PLACEHOLDER = '[name]'

with open(INVITEES) as invitees:
    guest = invitees.readlines()

for person in guest:
    with open(TEMPLATE) as letter:
        person = person.strip()
        content = letter.read()
        content = content.replace(PLACEHOLDER, person)
        with open(f'Output/ReadyToSend/{person}.txt', 'w') as outgoing:
            outgoing.write(content)
