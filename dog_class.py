# Abstract and create the Class Dog


class Dog:

    def __init__(self, name, breed, size):
        self.name = name
        self.breed = breed
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
