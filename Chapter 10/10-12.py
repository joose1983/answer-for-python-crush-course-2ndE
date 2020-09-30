import json


filename= 'favorite_number.txt'
try:
    with open(filename) as f:
        favorite_num=json.load(f)
except FileNotFoundError:
    favorite_num=input("What is your favorite number?")
    try:
        favorite_num=int(favorite_num)
    except ValueError:
        print("You must input a number.")
    else:
        with open(filename, 'w') as f:
            json.dump(favorite_num,f)
        print("Next time I'll remember it!")
else:
    print(f"I know your favorite number, it is {favorite_num}")





