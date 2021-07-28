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


def is_resources_sufficient(ordered_ingredients):
    for item in ordered_ingredients:
        if ordered_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
        else:
            return True


def process_coins():
    print("Please insert coins.")
    quarters = float(input("How many quarters?: "))
    dimes = float(input("how many dimes?: "))
    nickles = float(input("how many nickles?: "))
    pennies = float(input("how many pennies?: "))
    total = (quarters * 0.25) + (dimes * 0.10) + (nickles * 0.05) + (pennies * 0.01)
    return total


profit = 0
is_on = True
while is_on:
    user_choice = input("What would you like? (espresso/latte/cappuccino): ")
    if user_choice == "off":
        is_on = False
    elif user_choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")

    else:
        drink = MENU[user_choice]
        if is_resources_sufficient(drink["ingredients"]):
            total_coins = process_coins()
            product_cost = float(drink["cost"])
            if total_coins == product_cost:

                print(f"“Here is your {user_choice}☕️. Enjoy!")
            elif total_coins > product_cost:
                refund = float(round((total_coins - product_cost), 2))
                print(f"Here is ${refund} dollars in change.")
                print(f"“Here is your {user_choice}☕️. Enjoy!")

            else:
                print("Sorry that's not enough money. Money refunded.")
            profit += round(total_coins, 2)

        else:
            is_on = False
