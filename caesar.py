# Returns the alphabet position of a given letter.
# Example:
# alphabet_position("h"): 7
def alphabet_position(letter):
    # String of lowercase letters
    lower_letters = "abcdefghijklmnopqrstuvwxyz"

    # String of uppercase letters
    upper_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    if letter.isupper():
        for letter_number in range(len(upper_letters)):
            if upper_letters[letter_number] == letter:
                return letter_number
    else:
        for letter_number in range(len(lower_letters)):
            if lower_letters[letter_number] == letter:
                return letter_number

# Rotates letter char to the letter rot letters away from letter char
# Example
# caesar.rotate_character("A", 5): 'F'
def rotate_character(char, rot):
    # String of lowercase letters
    lower_letters = "abcdefghijklmnopqrstuvwxyz"

    # String of uppercase letters
    upper_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    # Keep number of shifts done
    #

    # If the character is a letter, shift it by rot
    if char.isalpha():
        # Create variable for char's alphabet position
        char_position = alphabet_position(char)
        if char.isupper():
            return upper_letters[char_position + (int(rot) % 26)]
        else:
            return lower_letters[char_position + (int(rot) % 26)]
    # If char is not a letter, return it unchanged
    else:
        return char

# Encrypts all letters in text by rot letters
# Example: 
#
# def encrypt(text, rot):
