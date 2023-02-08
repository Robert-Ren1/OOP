import random


class Insect:

    def __init__(self):
        self.wing = 2
        self.legs = 4
        self.flight = 0

    def toss(self):
        self.flight = random.randint(1, 10)

    def get(self):
        return self.flight
