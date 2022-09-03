#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

#Easy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

#Hardcore Level - Don't use choice(), don't use append(),
#don't use shuffle().

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))


password = ""

for _ in range(0, nr_letters):
  i = random.randint(0, 51)
  letter = letters[i]
  password += letter
for _ in range(0, nr_symbols):
  i = random.randint(0, 8)
  symbol = symbols[i]
  password += symbol
for _ in range(0, nr_numbers):
  i = random.randint(0, 9)
  number = numbers[i]
  password += number

the_password = ""
size = len(password)
list1=[]
list1[:0]=password

for a in range(0, size):
  size = len(list1)
  i = random.randint(0, size-1)
  password1 = list1[i]
  list1.pop(i)
  the_password += password1

print(the_password)



###Hard Level - Order of characters randomised:###
###e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P###

# password_list = []

# for char in range(1, nr_letters + 1):
#   password_list.append(random.choice(letters))

# for char in range(1, nr_symbols + 1):
#   password_list += random.choice(symbols)

# for char in range(1, nr_numbers + 1):
#   password_list += random.choice(numbers)

# print(password_list)
# random.shuffle(password_list)
# print(password_list)

# password = ""
# for char in password_list:
#   password += char

# print(f"Your password is: {password}")


