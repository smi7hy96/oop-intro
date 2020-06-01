class Animal:

    def __init__(self, colour, name, breed, sleepy, age):
        self.colour = colour
        self.__name = name.title()
        self.breed = breed.title()
        self.sleepy = sleepy
        self.age = age

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def eat(self, food):
        return f'OOOH, {food.title()}'

    def sleep(self):
        if self.sleepy:
            self.sleepy = True
            return '*snore*'
        else:
            return 'No! I wanna play!'

    def happy_birthday(self):
        self.age += 1
        return f'Happy Birthday {self.get_name()}!! You are {self.age}!'
