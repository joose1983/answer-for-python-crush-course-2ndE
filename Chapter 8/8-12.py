def sandwich_ordering(*toppings):
    print("you have ordered sandwiches with the following toppings.")
    for topping in toppings:
        print(f"- {topping}")
    print('\n')
    
sandwich_ordering('potatos','beef','onion','sugar')
sandwich_ordering('beef')
sandwich_ordering('shrimp','tomato')
