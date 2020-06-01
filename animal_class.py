class Animal:

    def __init__(self, colour, name, breed, sleepy, age):
        self.colour = colour
        self.__name = name.title()
        self.__breed = breed.title()
        self.sleepy = sleepy
        self.__age = age

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_age(self, age):
        self.__age = age

    def get_age(self):
        return self.__age

    def set_breed(self, breed):
        self.__breed = breed

    def get_breed(self):
        return self.__breed

    def eat(self, food):
        return f'OOOH, {food.title()}'

    def sleep(self):
        if self.sleepy:
            self.sleepy = True
            return '*snore*'
        else:
            return 'No! I wanna play!'

    def happy_birthday(self):
        self.set_age(self.get_age() + 1)
        return f'Happy Birthday {self.get_name()}!! You are {self.get_age()}!'
