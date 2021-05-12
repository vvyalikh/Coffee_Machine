

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
profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


process_is_on = True


def check_resources_foo(menu_ingredients):
    """Returns True if order can be made and False in ingredients are insufficient"""
    for item in menu_ingredients:
        if resources[item] < menu_ingredients[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


def process_coins():
    """Returns total of coins inserted"""
    price = MENU[user_choice]["cost"]
    print(f"The price of the drink is {price}")
    print("You can use: quarters($0.25), dimes($0.10), nickles($0.05), pennies($0.01)")
    quarters = int(input("How many quarters?\n "))
    dimes = int(input("How many quarters?\n "))
    nickles = int(input("How many quarters?\n "))
    pennies = int(input("How many quarters?\n "))
    coins_inserted = quarters*0.25 + dimes*0.10 + nickles*0.05 + pennies*0.01
    return coins_inserted


def is_transaction_successful(money_received, drink_cost):
    """Return True if payment is accepted and False is paid amount is not enough"""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is your ${change} change")
        global profit
        profit = profit + drink_cost
        return True
    else:
        print("Sorry, that's not enough money. Money refunded")
        return False


def make_coffee(choice, ingredients):
    """Deduct required ingredients from the resources"""
    for item in ingredients:
        resources[item] -= ingredients[item]
    print(f"Here is your drink {choice} ☕. Enjoy!")


while process_is_on:
    user_choice = input("What would you like? (espresso/latte/cappuccino): \n")
    if user_choice == 'off':
        process_is_on = False
        print("Power off")
    elif user_choice == 'report':
        print(f" Water: {resources['water']} \n Coffee: {resources['coffee']}\n "
              f"Milk: {resources['milk']} \n Money: {profit}")
        process_is_on = False
    else:
        drink = MENU[user_choice]
        if check_resources_foo(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(user_choice, drink["ingredients"])
