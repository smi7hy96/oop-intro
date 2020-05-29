# Abstract and create the Class Dog


class Dog:

    def __init__(self, name):
        self.name = name

    def bark(self):
        return f'{self.name}, bark'