alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").strip()
text = input("Type your message:\n").lower().strip()
shift = int(input("Type the shift number:\n"))
encrypted = []
decrypted = []

def encryption(_text, _shift):
    for letter in _text:
        shift_number = alphabet.index(letter) + _shift
        encrypted.append(alphabet[shift_number])
        
    print("The encoded text is: ","".join(encrypted))
    
def decryption(_text, _shift):
    for letter in _text:
        shift_number = alphabet.index(letter) - _shift
        decrypted.append(alphabet[shift_number])
    print("The decoded text is: ","".join(decrypted))    


if direction == "encode":
    print("encoding...")
    encryption(text, shift)
if direction == "decode":
    print("decoding...")
    decryption(text, shift)   