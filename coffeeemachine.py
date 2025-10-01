MENU = {
    "espresso" : {
        "ingredients": {
            "water" : 50,
            "coffee": 18,
        },
        "cost": 1.5
    },
    "latte" : {
        "ingredients": {
            "water" : 200,
            "coffee": 24,
            "milk": 150
        },
        "cost": 2.5
    },
    "cappuccino" : {
        "ingredients": {
            "water" : 250,
            "coffee": 24,
            "milk": 100
        },
        "cost": 3.0
    },
}

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100
}

def is_resource_suff(order_ingredients):
    for item in order_ingredients:
        if (order_ingredients[item] >= resources[item]):
            print(f"Sorry there is not enough {item}")
            return False
    return True

def process_coins():
    print("Please insert coins")
    total = int(input("how many quarters? : ")) * 0.25
    total += int(input("how many dimes? : ")) * 0.1
    total += int(input("how many nickles? : ")) * 0.10
    total += int(input("how many pennies? : ")) * 0.05
    return total

def is_enough_coins(Payment, drink_cost):
    if (Payment < drink_cost):
        print("Sorry that's not enough money. Money refunded.")
        return False
    else:
        change = round(Payment - drink_cost,2)
        print(f"Here is ${change} in change")
        global profit
        profit += drink_cost
        return True
  
def make_coffee(drink_name, ordre_ingredients):
    for item in ordre_ingredients:
        resources[item] -= ordre_ingredients[item]
    print(f"Here is your {drink_name}")

is_on = True



while is_on:
    user_input = input("What would you like?(espresso/latte/cappuccino)")
    if (user_input == "off"):
        is_on = False
    elif (user_input == "report"):
        print(f"Water : {resources['water']}ml")
        print(f"Milk : {resources['milk']}ml")
        print(f"Coffee : {resources['coffee']}g")
        print(f"Money : ${profit}")
    else:
        drink = MENU[user_input]
        print(drink)
        if (is_resource_suff(drink["ingredients"])):
            payment = process_coins()
            if(is_enough_coins(payment, drink['cost'])):
                make_coffee(user_input, drink['ingredients'])