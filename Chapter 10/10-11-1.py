import json

filename= 'favorite_number.txt'
try:
    with open(filename) as f:
        favorite_num=json.load(f)
except FileNotFoundError:
    print(f"{filename} not found.")
else:
    print(f"I know your favorite number, it is {favorite_num}")
