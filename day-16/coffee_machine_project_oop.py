#!/usr/bin/env python3
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()


def admin(action):
    if action == "off":
        exit(0)
    if action == "report":
        coffee_maker.report()
        money_machine.report()


def main():
    while True:
        # TODO: 1. Prompt the user for an action. REPEAT
        admin_actions = ['report', 'off']
        options = menu.get_items()
        action = input(f"What would you like? ({options}): ").lower()

        # TODO: 2. Allow for the machine to be turned off (cease program).
        # TODO: 3. Print report.
        if action in admin_actions:
            admin(action)
            continue
        elif menu.find_drink(action):
            drink = menu.find_drink(action)
        else:
            continue

        # TODO: 4. Check that resources are sufficient?
        if not coffee_maker.is_resource_sufficient(drink):
            continue

        # TODO: 5. Process coins.
        # TODO: 6. Check if transaction was successful?
        print("Price: ${:.2f}".format(drink.cost))
        if not money_machine.make_payment(drink.cost):
            continue

        # TODO: 7. Make coffee; deduct from resources.
        coffee_maker.make_coffee(drink)


if __name__ == "__main__":
    main()
