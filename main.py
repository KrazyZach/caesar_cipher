
from art import logo
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar(text, shift, direction):
    final_text = ""
    for letter in text:
        if letter not in alphabet:
            final_text += letter
        else:
            position = alphabet.index(letter)
            if direction == 'encode':
                new_position = position + shift
                final_text += alphabet[new_position]
            else:
                new_position = position - shift
                final_text += alphabet[new_position]  
    print(f"Here's the {direction}d result: {final_text}")

print(logo)
try_again = False
while try_again == False:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n")) 
    
    if shift > 26:
        shift %= 26
    caesar(text, shift, direction)
    again = input('Would you like to try again, Type Y or N:\n')
    if again.lower() == 'n' or again.lower() == 'no':
        try_again = True