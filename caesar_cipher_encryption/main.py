from assets import logo, alphabet

print(logo)

final_text = []
restart_cipher = True


while restart_cipher:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").strip()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n")) % 26
    def ceasar(_text, _shift, operator):
        if operator == "decode":
            _shift *= -1
        for letter in _text:
            if letter in alphabet:
                shift_number = alphabet.index(letter) + _shift
                final_text.append(alphabet[shift_number])
            else:
                final_text.append(letter)    
        print(f"Your {operator}d text is : ","".join(final_text)) 
    ceasar(text, shift, direction)
    final_text = []
    restart = input("Would you like to restart cipher?\nType 'yes' if you want to go again. Otherwise type 'no'. ").lower().strip()
    if restart == "no":
        restart_cipher = False
        print("Goodbye")

        