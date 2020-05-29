class Cat:

    def __init__(self, behaviour, colour, name, sleepy, breed):
        self.behaviour = behaviour
        self.colour = colour
        self.name = name
        self.sleepy = sleepy
        self.breed = breed

    def eat(self, food):
        return f'ugh, {food.title()}'

    def sleep(self):
        if self.sleepy:
            return '*snore*'
        else:
            return 'I wanna play!'

    def attack(self):
        if not self.sleepy:
            return 'HISS'
        else:
            return self.sleep()
