from coffeeoopmenu import Menu, MenuItem
from coffeemakeroop import CoffeeMaker
from coffeemoneyoop import MoneyMachine
money_machine = MoneyMachine()
coffee_making = CoffeeMaker()

is_on=True

while is_on:

    menu = Menu()
    options = menu.get_items()
    choice = input(f"What would you like to have {options}")
    if choice == "off":
        is_on = False
    elif choice == "report":
        money_machine.report()
        coffee_making.report()
    else:
        drink = menu.find_drink(choice)
        if coffee_making.is_resource_sufficient(drink):
            money_machine.make_payment(drink.cost)
            coffee_making.make_coffee(drink)
