# Abstract and create the Class Dog
from animal_class import *


class Dog(Animal):

    def __init__(self, colour, name, breed, sleepy, age, size):
        super().__init__(colour, name, breed, sleepy, age)
        self.size = size

    def bark(self):
        return f'{self.size} bark'

    def eat(self, food):
        return 'oooh, ' + food.lower()

    def sleep(self):
        return '*snore*'

    def fetch(self, item):
        if item == "ball":
            return "CHAAAASE"
        elif item == "stick":
            return "GET THA STICK"
        else:
            return "*yawn* i'll sit back down"
