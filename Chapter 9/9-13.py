from random import randint

class Die:

    def __init__(self, sides = 6):
        self.sides = sides

    def roll_die(self):
        print(randint(1,self.sides))


my_die = Die(6)
      
for roll in range(10):
    my_die.roll_die()
print("-------------------------")

my_die1 = Die(10)
for roll in range(10):
    my_die1.roll_die()
    
print("-------------------------")    
my_die2 = Die(20)
for roll in range(10):
    my_die1.roll_die()
