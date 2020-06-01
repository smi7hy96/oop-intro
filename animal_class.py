class Animal:

    def __init__(self, colour, name, breed, sleepy):
        self.colour = colour
        self.name = name
        self.breed = breed
        self.sleepy = sleepy

    def eat(self, food):
        return f'ugh, {food.title()}'

    def sleep(self):
        if self.sleepy:
            self.sleepy = True
            return '*snore*'
        else:
            return 'I wanna play!'