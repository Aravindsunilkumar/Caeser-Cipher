# Creating a list of Alphabets
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
#Asking the user either encode or decode the message
cipher_direction = input("Type 'Encode' for encodeing and 'Decode' for Decoded the message: \n")
#Enter the desired message
text = input('Type your message:\n').lower()
shift=int(input('Type the shift number'))
def caeser(start_text,shift_amount,cipher_direction):
    end_text=""
    if cipher_direction == 'decode':
            shift_amount *= -1
    for letter in start_text:
        position = alphabet.index(letter)
        new_positon = position +shift_amount
        end_text += alphabet[new_positon]
    print(f"the {cipher_direction} of the text {end_text}")
caeser(start_text= text, shift_amount=shift,cipher_direction=cipher_direction)