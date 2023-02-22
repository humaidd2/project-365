from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
menu = Menu()
money_machine = MoneyMachine()

machine_off = False

while not machine_off:
    options = menu.get_items()
    user_choice = input(f"What would you like? ({options}): ")
    if user_choice == "report":
        coffee_maker.report()
        money_machine.report()
    elif user_choice == "off":
        machine_off = True
    else:
        drink = menu.find_drink(user_choice)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)

# from prettytable import PrettyTable
#
# table = PrettyTable()
# table.add_column("Pokemon Type", ["Humaid", 'Mahmood', "Man"])
# table.add_column("Type", ["Man", "Woman", "child"])
# table.align = "l"
# print(table)
