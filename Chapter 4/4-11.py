pizzas=['beef pizza','shrimp pizza','fish pizza']
friend_pizzas=pizzas[:]
pizzas.append('strawberry pizza')
friend_pizzas.append('icecream pizza')
print("My favorate pizzas are:")
for pizza in pizzas:
    print(pizza)
print("My friend pizzas are:")
for pizza in friend_pizzas:
    print(pizza)

