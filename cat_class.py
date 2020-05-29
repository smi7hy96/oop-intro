class Cat:

    def __init__(self, behaviour, colour, name, sleepy, breed):
        self.behaviour = behaviour
        self.colour = colour
        self.name = name
        self.sleepy = sleepy
        self.breed = breed

    def eat(self, food):
        return f'ugh, {food.title()}'
