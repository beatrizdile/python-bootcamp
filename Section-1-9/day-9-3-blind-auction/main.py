from replit import clear
import art
#You can call clear() to clear the output in the console.

print(art.logo)
print("Wlcome to the secret auction program.")

all_bids = {}

def new_bid ():
    name = input("What is your name?: ")
    bid = input("What's your bid?: $")
    all_bids[name] = bid
    again = input("Are there any other bidders? Type 'yes' or 'no'. \n").lower()
    if again == "yes":
        clear()
        new_bid()   

new_bid()

highest_bid = 0
winner = ""

for name in all_bids:
    if int(all_bids[name]) > highest_bid:
        highest_bid = int(all_bids[name])
        winner = name

clear()
print(f"The winner is {winner} with a bid of ${highest_bid}.")

print(all_bids)

