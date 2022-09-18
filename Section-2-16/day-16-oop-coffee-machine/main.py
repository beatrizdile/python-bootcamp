from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money = MoneyMachine()
coffee_machine = CoffeeMaker()
items = Menu()

while True:
    the_drink = input(f"What would you like? {items.get_items()}: ").lower()
    if the_drink == "report":
        coffee_machine.report()
        money.report()
        continue
    if the_drink == "off":
        break
    menu_item = items.find_drink(the_drink)
    if menu_item is None:
        continue
    elif not coffee_machine.is_resource_sufficient(menu_item):
        continue
    elif not money.make_payment(menu_item.cost):
        continue
    else:
        coffee_machine.make_coffee(menu_item)
