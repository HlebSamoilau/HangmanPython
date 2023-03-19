alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def caesar(start_text, shift_val, cipher_direction):
    shift_val = shift_val % len(alphabet)
    encoded_text = ""
    for sign in start_text:
        if sign not in alphabet:
            encoded_text += sign
        else:
            pos = alphabet.index(sign)
            if cipher_direction == "encode":
                pos = pos + shift_val
                if pos >= len(alphabet):
                    pos = pos - len(alphabet)
            elif cipher_direction == "decode":
                pos = pos - shift_val
                if pos < 0:
                    pos = len(alphabet) + pos
            else:
                print("You choose wrong parameters!")
                break
            encoded_text += alphabet[pos]

    print(f"The {cipher_direction}d text is '{encoded_text}'")


while True:
    caesar(start_text=text, shift_val=shift, cipher_direction=direction)

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt, type 'q' for exit:\n")
    if direction == "q":
        print("Goodbye")
        break
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
