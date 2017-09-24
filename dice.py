import random

class Die:
    def __init__(self, sides=2, value=0):
        if not sides >= 2:
            raise ValueError("Must have at lease 2 sides.")
        if not isinstance(sides,int):
            raise ValueError("Sides must be whole number.")
        self.value = value or random.randint(1,sides)

        #return an instance of Die into an integer
    def __int__(self):
        return self.value

    def __eq__(self,other):
        return int(self) == other
    def __ne__(self,other):
        return int(self) != other

    #turning self into int, then comparing to another value
    def __gt__(self, other):
        return int(self) > other
    def __lt__(self,other):
        return int(self) < other

    def __ge__(self,other):
        return int(self) >= other
    def __le__(self,other):
        return int(self) <= other

    def __add__(self,other):
        return int(self) + other
    def __radd__(self,other):
        return int(self) + other

    def __repr__(self):
        return str(self.value)


class D6(Die):
    def __init__(self,value=0):
        super().__init__(sides=6, value=value)
