import random
from art import logo
#from replit import clear

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def sum_scores (cards):
    sum = 0
    for i in cards:
        sum = sum + i
    return sum

def draw():
    # player_cards.append(random.choice(cards))
    player_cards.append(10)
    
def comput_draw():
    # comput_cards.append(random.choice(cards))
    comput_cards.append(6)    
    
def the_numbers():
    player_score = sum_scores(player_cards)
    print(f"Your cards: {player_cards}, current score: {player_score}")
    print(f"Computer's first card: {comput_cards[0]}")

def final_numbers():
    player_score = sum_scores(player_cards)
    print(f"Your final hand: {player_cards}, final score: {player_score}")

def final_comput():
    comput_score = sum_scores(comput_cards)
    print(f"Computer's final hand: {comput_cards}, final score: {comput_score}")

def ace():
    player_cards.remove(11)
    player_cards.append(1)

def comput(state):
    if sum_scores(comput_cards) < 17:
        comput_draw()
        comput(state)
    elif sum_scores(comput_cards) > 21 and state:
        final_numbers()
        final_comput()
        print("Opponent went over. You win")
    elif sum_scores(comput_cards) > sum_scores(player_cards) and state:
        final_numbers()
        final_comput()
        print("You lose")
    elif sum_scores(comput_cards) < sum_scores(player_cards) and state:
        final_numbers()
        final_comput()
        print("You win")
    elif sum_scores(comput_cards) == sum_scores(player_cards) and state:
        final_numbers()
        final_comput()
        print("Draw")
    else:
        final_numbers()
        final_comput()



def game():

    i = 1
    
    while(True):
        if i == 1:
            if player_score == 21 and comput_score == 21:
                final_numbers()
                comput(False)
                print("Draw")
                break
            elif 11 in player_cards and 10 in player_cards:
                final_numbers()
                comput(False)
                print("You win, Blackjack")
                break
            elif 11 in comput_cards and 10 in comput_cards:
                final_numbers()
                comput(False)
                print("You lose, Blackjack")
                break
            else:
                i += 1
        elif sum_scores(player_cards) > 21:
            if 11 in player_cards:
                ace()
                the_numbers()
                if sum_scores(player_cards) > 21:
                    comput(False)
                    print("You went over. You lose")
                    break
                elif input("Type 'y' to get another card, type 'n' to pass: ") == "y":
                    draw()
                    #the_numbers()
                    continue
                else:
                    break
            else:
                comput(False)
                print("You went over. You lose")
                break
        elif input("Type 'y' to get another card, type 'n' to pass: ") == "y":
            draw()
            continue
        else:
            comput(True)


    


play = True

while (play):
    if input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
        #clear()
        print(logo)
        # player_cards = random.choices(cards, k = 2)
        # comput_cards = random.choices(cards, k = 2)
        player_cards = [9, 11]
        comput_cards = [10, 5]
        player_score = sum_scores(player_cards)
        comput_score = sum_scores(comput_cards)
        
        the_numbers()
        game()
    else:
        play = False





    
