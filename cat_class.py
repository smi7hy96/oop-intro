from animal_class import *


class Cat(Animal):

    def __init__(self, behaviour, colour, name, sleepy, breed):
        self.behaviour = behaviour.title()
        self.colour = colour
        self.name = name
        self.breed = breed
        self.sleepy = sleepy

    def attack(self):
        if not self.sleepy or self.behaviour == "Aggressive":
            self.sleepy = True
            return 'HISS'
        else:
            return self.sleep()

    def chase(self, animal):
        if animal == 'mouse':
            self.sleepy = True
            return 'Come here Jerry'
        else:
            return 'Not interested'

    def play(self, item):
        if item == 'box':
            return 'If I fits....'
        else:
            return "Erm no. Where's the box?"
