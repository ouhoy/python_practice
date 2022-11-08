alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").strip()
text = input("Type your message:\n").lower().strip()
shift = int(input("Type the shift number:\n"))
final_text = []

def ceasar(_text, _shift, operator):
  
    if operator == "decode":
        _shift *= -1
    for letter in _text:
        shift_number = alphabet.index(letter) + _shift
        final_text.append(alphabet[shift_number])
    print(f"Your {operator}d text is : ","".join(final_text)) 
ceasar(text, shift, direction)