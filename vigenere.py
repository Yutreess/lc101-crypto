# Allows using rotate_character and alphabet_position functions
from helpers import rotate_character, alphabet_position

# Encrypts text using the Vigenere Cypher.
# text: "The crow flies at midnight!"
# wordKey: boom
# result: Uvs osck rmwse bh auebwsih!
def encrypt(text, word_key):
  # List to contain encrypted text
  crypted_list = list(text)

  # String to contain crypted_text
  crypted_text = ""

  # List to contain the word_key
  word_key_list = []

  # Word key letter position
  word_key_pos = 0

  # Fill the list with the word_key
  for letter in crypted_list:

    if letter.isalpha():
      word_key_list.append(word_key[word_key_pos])
      word_key_pos += 1
      # Return position to zero if the last letter was used
      if word_key_pos == len(word_key):
        word_key_pos = 0
    else:
      word_key_list.append(letter)
  
  # Shift characters in crypted_list
  for index, char in enumerate(crypted_list):
    if char.isalpha():
      crypted_list[index] = rotate_character(char, alphabet_position(word_key_list[index]))

  # Add everything from crypted_list to crypted_text
  for char in crypted_list:
    crypted_text += char
  #print(word_key_list)
  return str(crypted_text)

def main():
  from sys import argv, exit
  for char in argv[1]:
    if not char.isalpha():
      print("usage: python vigenere.py [ENCRYPTION WORD KEY]")
      print("ENCRYPTION WORD KEY: SHould be only alpha characters. No numbers or symbols.")
      exit()
  word_key = str(argv[1])
  text = str(input("Type a message:\n"))
  print(encrypt(text, word_key))

if __name__ == "__main__":
  main()