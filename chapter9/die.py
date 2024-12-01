from random import randint
class Die:

    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        roll_value = randint(1, self.sides)
        return roll_value
    
standard_die = Die()
print(standard_die.roll_die())
dnd_die = Die(20)
print(f"{dnd_die.roll_die()}")