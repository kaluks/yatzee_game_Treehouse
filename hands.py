from dice import D6

class Hand(list):
    def __init__(self, size=0, die_class=None, *args, **kwargs):
        #size is nmbr of dice, die_class is D6 or D5 or etc
        if not die_class:
            raise ValueError("must provide a die class.")
        super().__init__()

        for _ in range(size):
            self.append(die_class())
            #this creates how ever many instances
            #of dice that were entered in size
            #ie, 4 dice created if size=4
        self.sort()

    def _by_value(self,value):
        dice = []
        for die in self:
            if die == value:
                dice.append(die)
        return dice

class YatzeeHand(Hand):
    def __init__(self, *args, **kwargs):
        super().__init__(size=5, die_class=D6, *args, **kwargs)

    @property
    def ones(self):
        return self._by_value(1)
    @property
    def twos(self):
        return self._by_value(2)
    @property
    def threes(self):
        return self._by_value(3)
    @property
    def fours(self):
        return self._by_value(4)
    @property
    def fives(self):
        return self._by_value(5)
    @property
    def sixes(self):
        return self._by_value(6)

    @property
    def _sets(self):
        return {
            1: len(self.ones),
            2: len(self.twos),
            3: len(self.threes),
            4: len(self.fours),
            5: len(self.fives),
            6: len(self.sixes)}
