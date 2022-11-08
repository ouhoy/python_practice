alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
encrypted = []
decrypted = []

def encryption(_text, _shift):
    for letter in _text:
        shift_number = alphabet.index(letter) + _shift
        if shift_number > len(alphabet) - 1:
            encrypted.append(alphabet[+ _shift -(len(alphabet) + 1)])
        else:
            encrypted.append(alphabet[shift_number])
        
    print("".join(encrypted))
def decryption(_text, _shift):
    print()


if direction.strip() == "encode":
    print("encoding...")
    encryption(text, shift)
if direction.strip() == "decode":
    decryption(text, shift)   