# Allows using rotate_character and alphabet_position functions
from helpers import rotate_character, alphabet_position

# Encrypts all letters in text by rot letters
def encrypt(text, rot):
    crypted_text = ''
    for char in text:
        crypted_text += rotate_character(char, rot)
    return crypted_text

def main():
    from sys import argv, exit
    if argv[1].isdigit():
        rotation = int(argv[1])
    else:
        print("usage: python caesar.py [INTEGER VALUE]")
        exit()
    text = str(input("Type a message:\n"))
    print(encrypt(text, rotation))
    
if __name__ == "__main__":
    main()