MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
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
}

money = 0


def report(resource, money_available):
    print(f"Water: {resources['water']}ml\nMilk: {resource['milk']}ml\nCoffee: "
          f"{resource['coffee']}g\nMoney: ${money_available}")
    return


def resource_sufficient(choice, resource):
    global MENU
    enough = True
    item = MENU[choice]['ingredients']
    for i, j in resource.items():
        if item[f"{i}"] > j:
            print(f"Sorry, there is not enough {i}")
            enough = False

    return enough


def process_coins(quarters, dimes, nickels, pennies, drink):
    global MENU
    global money
    quarters = quarters * 0.25
    dimes = dimes * 0.1
    nickels = nickels * 0.05
    pennies = pennies * 0.01

    money_inserted = quarters + dimes + nickels + pennies
    if money_inserted < MENU[drink]['cost']:
        print("sorry, that's not enough money, money refunded")
        return False

    else:
        change = money_inserted - MENU[drink]['cost']
        print(f"Here is ${change} in change.")
        money += MENU[drink]['cost']
        return True


def make_coffee(choice, resources_available):
    global MENU

    for i in resources_available:
        resources_available[i] -= MENU[choice]['ingredients'][f"{i}"]

    print(f"Here is your {choice}. Enjoy!")
    return


machine_off = False
while not machine_off:
    user_choice = input("What would you like? (espresso/latte/cappuccino): ")
    if user_choice == "report":
        report(resources, money)
    elif user_choice == "off":
        machine_off = True
    elif user_choice == "latte" or "espresso" or "cappuccino":

        is_resource_sufficient = resource_sufficient(user_choice, resources)
        if is_resource_sufficient:
            print("Please insert coins")
            q = int(input("How many quarters?: "))
            d = int(input("How many dimes?: "))
            n = int(input("How many nickels?: "))
            p = int(input("How many pennies?: "))
            is_money_enough = process_coins(q, n, d, p, user_choice)
            if is_money_enough:
                make_coffee(user_choice, resources)
    else:
        print("Invalid Prompt. Try again")
