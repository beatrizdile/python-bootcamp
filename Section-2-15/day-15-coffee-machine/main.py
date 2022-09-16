MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk": 0,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0,
}


def report():
    for item in resources:
        print(f"{item.capitalize()}: {resources[item]}")


def make_coffee(drink):
    for item in resources:
        if item == "money":
            resources["money"] = resources["money"] + MENU[drink]["cost"]
            continue
        else:
            resources[item] = resources[item] - MENU[drink]["ingredients"][item]
    print(f"Here is your {drink}. Enjoy!")


def money(drink):
    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    total_money = (quarters*0.25)+(dimes*0.10)+(nickles*0.05)+(pennies*0.01)
    if total_money < MENU[drink]["cost"]:
        print("Sorry that's not enough money. Money refunded.")
    elif total_money > MENU[drink]["cost"]:
        total_money = total_money - MENU[drink]["cost"]
        total_money = "{:.2f}".format(total_money)
        print(f"Here is {total_money} dollars in change.")
        make_coffee(drink)
    else:
        make_coffee(drink)


def check_resources(drink):
    for item in resources:
        if item == "money":
            continue
        elif resources[item] < MENU[drink]["ingredients"][item]:
            return print(f"Sorry there is not enough {item}.")
    money(drink)


while True:
    the_drink = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if the_drink == "espresso" or the_drink == "latte" or the_drink == "cappuccino":
        check_resources(the_drink)
    elif the_drink == "off":
        break
    elif the_drink == "report":
        report()
    else:
        print("Invalid")
        continue
