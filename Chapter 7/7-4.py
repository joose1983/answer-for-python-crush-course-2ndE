active = True
while active:
    topping = input("Please input the toppings you required: ")
    if topping=='quit':
        active = False
    else:
        print("You'll add this topping to you pizza.")
