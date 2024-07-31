from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()


def print_report():
    coffee_maker.report()
    money_machine.report()


def make_coffee():
    menu = Menu()
    menu_items = menu.get_items()
    menu_items = menu_items[0: (len(menu_items) - 1)]

    user_request = input(f"What would you like? ({menu_items}): ")
    selected_drink = menu.find_drink(user_request)

    is_enough_res = coffee_maker.is_resource_sufficient(drink=selected_drink)

    if is_enough_res:
        is_successful_tra = money_machine.make_payment(cost=selected_drink.cost)

        if is_successful_tra:
            coffee_maker.make_coffee(selected_drink)


def main_menu() -> bool:
    print("1. Turn off the Coffee Machine.")
    print("2. Print Report.")
    print("3. Make coffee.")
    user_request = int(input("What do you want to do? Type '1', '2', or '3': "))
    while user_request < 1 or user_request > 3:
        user_request = int(input("Please enter 1, 2, 3 to continue: "))

    if user_request == 1:
        return False
    elif user_request == 2:
        print_report()
    elif user_request == 3:
        make_coffee()

    return True


is_on = True

while is_on:
    is_on = main_menu()

    if not is_on:
        break
