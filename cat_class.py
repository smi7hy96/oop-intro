from animal_class import *


class Cat(Animal):

    def __init__(self, behaviour, colour, name, sleepy, breed, age):
        super().__init__(colour, name, breed, sleepy, age)
        self.behaviour = behaviour.title()

    def attack(self):
        if self.__mood():
            self.sleepy = True
            return 'HISS'
        else:
            return self.sleep()

    def __mood(self):
        if not self.sleepy or self.behaviour == "Aggressive":
            return True
        else:
            return False

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

    def eat(self, food):
        if self.sleepy:
            return "Really? Im trying to sleep here"
        else:
            return f'OOOH, {food.title()}'
