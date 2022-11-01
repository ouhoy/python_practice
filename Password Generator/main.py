#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

generated_letters = ""
genrated_numbers = ""
genrated_symbols = ""
generated_password = []
for i in range(0, nr_letters):
    random_letter =  random.randint(0, len(letters) - 1)
    generated_letters  += letters[random_letter]
    generated_password.append(letters[random_letter])

for n in range(0, nr_numbers):
    random_number =  random.randint(0, len(numbers) - 1)
    genrated_numbers  += numbers[random_number]
    generated_password.append(numbers[random_number])

for l in range(0, nr_symbols):
    random_symbol =  random.randint(0, len(symbols) - 1)
    genrated_symbols  += symbols[random_symbol]
    generated_password.append(symbols[random_symbol])

edited_password = generated_password
final_password = ""
num_count = 0
for m in range(0,len(generated_password)):
    num_count+= 1
    random_num = random.randint(0,  len(edited_password) - 1)
    final_password += edited_password[random_num]
    edited_password.pop(random_num)


print(final_password)    
