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

coins = {
    "penny": 0.01,
    "nickle": 0.05,
    "dime": 0.10,
    "quarter": 0.25,
}

keep_going = True


def app():
    while keep_going:
        # todo: Ask user what they want and put it in a variable
        user_input = input("What would you like? (espresso/latte/cappuccino) ").lower()

        if user_input == "report":
            for x in resources:
                if x == "water" or x == "milk":
                    print(f"{x}: {resources[x]}ml")
                else:
                    print(f"{x}: {resources[x]}g")
            app()

        # This will check if the resources is enough to continue the program, if not it will restart the program.
        for element in MENU:
            if user_input == element:
                for ingredient in resources:
                    if ingredient in MENU[user_input]["ingredients"]:
                        if resources[ingredient] < MENU[user_input]["ingredients"][ingredient]:
                            print(f"Not enough {ingredient}")
                            app()
        # End of resource check

        print("Please insert money")

        # todo: Make a variable for each coin asking the user how many they want to spend
        quarter_input = int(input("How many quarters? "))
        dime_input = int(input("How many dimes? "))
        nickle_input = int(input("How many nickles? "))
        penny_input = int(input("How many pennies? "))

        def money(quart=quarter_input, dime=dime_input, nickle=nickle_input, penny=penny_input):
            coin1 = coins["quarter"] * quart
            coin2 = coins["dime"] * dime
            coin3 = coins["nickle"] * nickle
            coin4 = coins["penny"] * penny
            return coin1 + coin2 + coin3 + coin4

        total_amount = money()

        # This will check if the user has enough money to buy drink and then deduct from resources for future drinks
        for element in MENU:
            if user_input == element:
                price = MENU[element]["cost"]
                if total_amount >= price:
                    for liquid in MENU[element]["ingredients"]:
                        resources[liquid] = resources[liquid] - MENU[element]["ingredients"][liquid]
                    print(f"Here's your change: ${total_amount - MENU[element]["cost"]}")
                    print(f"Here's your {user_input}. Enjoy!")
                else:
                    print("Sorry, that's not enough money. Money refunded")


app()
