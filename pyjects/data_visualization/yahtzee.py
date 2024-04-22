from random import randint
from typing import List
from die import Die

    
class Yahtzee:
    """Represents a game of yahtzee with 5 die and possible combinations of rolls"""

    def __init__(self) -> None:
        self.die1 = Die()
        self.die2 = Die()
        self.die3 = Die()
        self.die4 = Die()
        self.die5 = Die()
        self.yahtzee = 'Yahtzee'
        self.full_house = 'Full house'
        self.oak3 = '3 of a kind'
        self.oak4 = '4 of a kind'
        self.small_s = 'Small straight'
        self.large_s = 'Large straight'
        self.nothing = 'None'
        self.dice = [self.die1, self.die2, self.die3, self.die4, self.die5]


    def roll_em(self) -> List[int]:
        results = []
        for die in self.dice:
            results.append(die.roll())
        return results
    

    def _check_straight(self, to_check: List[int]):
        if len(set(to_check)) == len(to_check):
            return self.large_s
        elif len(set(to_check)) == len(to_check) - 1:
            return self.small_s
        else:
            return self.nothing
        

    def _check_dupes_and_straights(self, to_check: List[int]):
        for result in to_check:
            if to_check.count(result) == 5:
                return self.yahtzee
            elif to_check.count(result) == 4:
                return self.oak4
            elif to_check.count(result) == 3:
                return self.oak3
            elif self._check_straight(to_check):
                return self._check_straight(to_check)
            else:
                return self.nothing


    def interpret_results(self, results: List[int]):
        return self._check_dupes_and_straights(results)
