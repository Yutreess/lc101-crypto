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

    # If the character is a letter, shift it by rot
    if char.isalpha():
        # Create variable for char's alphabet position
        char_position = alphabet_position(char)

        # Keep number of shifts done
        num_shifts = 0

        # Shifted character
        shifted_char = char

        if char.isupper():
            while num_shifts < rot:
                num_shifts += 1
                if alphabet_position(shifted_char) == 25:
                    shifted_char = upper_letters[0]
                else:
                    shifted_char = upper_letters[alphabet_position(shifted_char) + 1]
            return shifted_char
        else:
            while num_shifts < rot:
                num_shifts += 1
                if alphabet_position(shifted_char) == 25:
                    shifted_char = lower_letters[0]
                else:
                    shifted_char = lower_letters[alphabet_position(shifted_char) + 1]
            return shifted_char
    # If char is not a letter, return it unchanged
    else:
        return char