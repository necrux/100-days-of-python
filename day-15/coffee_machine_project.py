#!/usr/bin/env python3
from os import system

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
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
    "money": 0.0,
}


def print_report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${resources['money']}")


def have_resources(ingredients):
    """Returns True if we have the ingredients available."""
    for item in ingredients:
        if ingredients[item] > resources[item]:
            print(f'Sorry, there is not enough {item}.')
            return False
    return True


def process_coins(action):
    """Returns True if enough money was inserted; makes changes as needed."""
    # TODO: 5. Process coins.
    print('Please insert coins.')
    payment = int(input('How many quarters?: ')) * .25
    payment += int(input('How many dimes?: ')) * .1
    payment += int(input('How many nickles?: ')) * .05
    payment += int(input('How many pennies?: ')) * .01

    price = MENU[action]['cost']
    if payment < price:
        print('Not enough money. Please insert at least {:.2f}. Money refunded.'.format(price))
        return False
    elif payment > price:
        change = round(payment - price, 2)
        print(f'Here is ${change} in change.')
    return True


def get_drink():
    action = input("What would you like? (espresso/latte/cappuccino): ").lower()
    return action


def main():
    while True:
        # TODO: 1. Prompt the user for an action. REPEAT
        action = 'none'
        actions = ['off', 'report', 'espresso', 'latte', 'cappuccino']
        while action not in actions:
            action = get_drink()

        # TODO: 2. Allow for the machine to be turned off (cease program).
        if action == "off":
            exit(0)

        # TODO: 3. Print report.
        if action == "report":
            print_report()
            continue

        # TODO: 4. Check that resources are sufficient?
        if not have_resources(MENU[action]['ingredients']):
            continue

        # TODO: 6. Check if transaction was successful?
        if process_coins(action):
            print(f'Here is your {action} ☕, enjoy!')

            # TODO: 7. Make coffee; deduct from resources.
            resources['water'] -= MENU[action]['ingredients']['water']
            resources['milk'] -= MENU[action]['ingredients']['milk']
            resources['coffee'] -= MENU[action]['ingredients']['coffee']
            resources['money'] += MENU[action]['cost']


if __name__ == '__main__':
    system('clear')
    main()
