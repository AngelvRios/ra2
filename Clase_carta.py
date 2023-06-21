import random

class carta:
    def __init__(self, character):
        self.character = character
        self.vida = random.randint(50, 300)
        self.poder = random.randint(5, 25)