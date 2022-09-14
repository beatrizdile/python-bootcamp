#my list of to-do:
#print arts
#pick two random instagram accounts
#show both of them and their information
#ask which has higher following and compare
#if correct keep the option B and pick a random new account
#if wrong end game
#track points

import art
import random
from game_data import data
from replit import clear


def random_number():
    num = random.randrange(0, 50)
    return num

def to_print(num):
    return f"{data[num]['name']}, {data[num]['description']}, from {data[num]['country']}"
    
def the_answer(num1, num2, answer):
    if data[num1]['follower_count'] > data[num2]['follower_count'] and answer == "a":
        return True
    elif data[num1]['follower_count'] < data[num2]['follower_count'] and answer == "b":
        return True
    else:
        return False
        

num1 = random_number()
num2 = random_number()
while num1 == num2:
    num2 = random_number()
points = 0
print(art.logo)

while True:
    print(f"Compare A: {to_print(num1)}")
    print(art.vs)
    print(f"\nAgainst B: {to_print(num2)}")
    
    answer = input("Who has more followers? Type 'A' or 'B': ").lower()
    clear()
    print(art.logo)
    
    if the_answer(num1, num2, answer):
        points += 1
        num1 = num2
        num2 = random_number()
        print(f"You're right! Current score: {points}.")
    else:
        print(f"Sorry, that's wrong. Final score: {points}")
        break

    
    