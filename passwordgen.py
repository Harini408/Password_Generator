import random
characters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']  
symbols = ['!', '@', '#', '$', '%', '&', '*'] 
input_ch = int(input("Enter the number of characters you want: "))
input_num = int(input("Enter the number of numbers you want: "))
input_sym = int(input("Enter the number of symbols you want: "))
password = []

for i in range(input_ch):
    password += random.choice(characters)
    
for i in range(input_num):
    password += random.choice(numbers)
    
for i in range(input_sym):
    password += random.choice(symbols)

random.shuffle(password)
total_length = input_ch + input_num + input_sym
print("Total length:", total_length)

final_password = "".join(password)
print("Your final password:", final_password)
print("Thank you for using our Password Generator!")



