print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

names = name1+name2
names_lower = names.lower()

T = names_lower.count("t")
R = names_lower.count("r")
U = names_lower.count("u")
E = names_lower.count("e")

score1 = T+R+U+E
print(score1)

L = names_lower.count("l")
O = names_lower.count("o")
V = names_lower.count("v")
E = names_lower.count("e")

score2 = L+O+V+E
print(score2)

score3 = int(str(score1)+str(score2))
print(score3)

if score3 < 10 or score3 > 90:
  print(f"Your score is {score3}, you go together like coke and mentos.")
elif score3 >= 40 and score3 <= 50:
  print(f"Your score is {score3}, you are alright together.")
else:
  print(f"Your score is {score3}.")



