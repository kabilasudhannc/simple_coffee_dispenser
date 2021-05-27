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

collection = 0


def money_calculator(money):
    money_values = {'quarter': 0.25, 'dime': 0.10, 'nickel': 0.05, 'penny': 0.01}
    total = 0
    for keys in money_values:
        total += money_values[keys] * money[keys]
    return total


def check_resource(choice):
    is_available = ''
    for ingredients in MENU[choice]['ingredients']:
        if resources[ingredients] > MENU[choice]['ingredients'][ingredients]:
            is_available = 'available'
        else:
            is_available = ingredients
            break
    return is_available


def manage_resource(choice):
    global resources
    ingredients = MENU[choice]['ingredients']
    for resource in ingredients:
        resources[resource] -= ingredients[resource]
    return resources


def report():
    for ingredients, balance in resources.items():
        print(f"{ingredients}: {balance} ml")
    print(f"Money: ${collection}")


def coffee_dispenser():
    global collection
    money = {'quarter': 0, 'dime': 0, 'nickel': 0, 'penny': 0}
    choice = input('\tWhat would you like? (espresso/latte/cappuccino): ').lower()
    if choice == 'report':
        report()

    else:
        is_available = check_resource(choice)
        if is_available == 'available':
            if choice in MENU:
                print('Please insert coins.')
                for keys in money:
                    value = int(input(f"how many {keys}s?: "))
                    money[keys] = value
                total = money_calculator(money)
                if total > MENU[choice]['cost']:
                    manage_resource(choice)
                    collection += MENU[choice]['cost']
                    balance = total - MENU[choice]['cost']
                    print(f"Here is ${balance} in change.")
                    print(f"Here is your {choice} ☕ Enjoy!")
                else:
                    print("Sorry that's not enough money. Money refunded.")
            else:
                print('The coffee you chose is not available.')
        else:
            print(f'Sorry there is not enough {is_available}')
    coffee_dispenser()


coffee_dispenser()
