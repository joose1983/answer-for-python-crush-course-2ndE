import json

filename = 'favorite_number.txt'
favorite_num=input("What is your favorite number?")
try:
    favorite_num=int(favorite_num)
except ValueError:
    print("You must input a number.}")

with open(filename, 'w') as f:
    json.dump(favorite_num,f)

