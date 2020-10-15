from Lists import *

class Nothing:
    def __init__(self):
        pass

    def __str__(self):
        return "Nothing"

    def __eq__(self, other):
        return type(other) == Nothing

nothing = Nothing()

class Just:
    def __init__(self, x):
        self.x = x

    def __str__(self):
        return "Just (" + str(self.x) + ")"

    def __eq__(self, other):
        return type(other) == Just and self.x == other.x

def just(x):
    return Just(x)

def isJust(x):
    return type(x) == Just

def isNothing(x):
    return type(x) == Nothing
