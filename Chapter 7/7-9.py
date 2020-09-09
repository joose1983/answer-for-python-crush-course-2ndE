sandwich_orders = ['pastrami','chicken', 'beef', 'pastrami', 'pork', 'tomato', 'pastrami']
print("Sorry, the deli has run out of pastrami.")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
finished_sandwich=[]
for item in sandwich_orders:
    print(f"I made your {item} sandwich.")
    finished_sandwich.append(item)
print(f"sandwich orders are: {sandwich_orders}")
print(f"finished sandwich orders are: {finished_sandwich}")
