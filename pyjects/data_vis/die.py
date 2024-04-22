from random import randint
from typing import List


class Die:
    """Represents a single die"""

    def __init__(self, num_sides=6) -> None:
        self.num_sides = num_sides


    def roll(self):
        return randint(1, self.num_sides)