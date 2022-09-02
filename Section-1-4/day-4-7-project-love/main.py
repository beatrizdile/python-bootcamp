import random

list = input("Names of the people: ").split(", ")

random_number1 = random.randint(0, len(list)-1)
name1 = list[random_number1] 
list.remove(name1)

random_number2 = random.randint(0, len(list)-1)
name2 = list[random_number2] 
list.remove(name2)

print(f"\nO casal da vez é: {name1} & {name2}")