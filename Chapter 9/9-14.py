from random import randint
from random import sample


lottery=""
letter=""
#generate a string list composed of 10 numbers and 5 letters


for i in range(0,10):
    number=str(randint(0,9))
    lottery= lottery + number
    
for i in range(0,5):
    letter=chr(randint(97,122))
    lottery= lottery + str(letter)
    
print(f"the lottery pool list is:{lottery}")
winner=sample(lottery,4)
print("Any ticket matching the following string shall get the prize")

print("".join(winner))




