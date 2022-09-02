import random

rock1 = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper1 = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors1 = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

list = ["rock", "paper", "scissors"]

person = input("What do you choose? Type Rock, Paper or Scissors. ").lower()

computer = random.choice(list)

if person == "rock":
  print(rock1)
elif person == "paper":
  print(paper1)
elif person == "scissors":
  print(scissors1)
else:
  print("You didn't pick one")
  exit() 


print("Computer chose: ")

if computer == "rock":
  print(rock1)
elif computer == "paper":
  print(paper1)
elif computer == "scissors":
  print(scissors1)


if person == "rock" and computer == "paper":
  print("You lose")
elif person == "rock" and computer == "rock":
  print("It's a draw")
elif person == "rock" and computer == "scissors":
  print("You win")

elif person == "paper" and computer == "paper":
  print("It's a draw")
elif person == "paper" and computer == "rock":
  print("You win")
elif person == "paper" and computer == "scissors":
  print("You lose")

elif person == "scissors" and computer == "paper":
  print("You win")
elif person == "scissors" and computer == "rock":
  print("You lose")
elif person == "scissors" and computer == "scissors":
  print("It's a draw")

  

