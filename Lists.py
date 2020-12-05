from Maybe import *

class Nil:
    # def __rpow__(self, other):
    #     return List(other, self)

    def __eq__(self, other):
        return type(other) == Nil

    def __str__(self):
        return "{}"

    def __getitem__(self, i):
        return nothing


nil = Nil()

def showListHelper(list):
    if list == nil:
       return ""
    elif list.tail == nil:
       return str(list.head)
    else:
       return str(list.head) + ", " + showListHelper(list.tail)

def showList(list):
    return "{" + showListHelper(list) + "}"

# Вернуть just(x), если x - элемент списка xs под номером i, считая от нуля.
# Иначе вернуть nothing
def index(i, xs):
    if xs == nil:
       return nothing
    else:
       if i == 0:
          return just(xs.head)
       else:
          return index(i - 1, xs.tail)


class List:
    def __init__(self, x, xs):
        self.head = x
        self.tail = xs

    # def __rpow__(self, other): # other ** self => List(other, self)
    #     return List(other, self)

    def __str__(self):
        return showList(self)

    def __eq__(self, other):
        return type(other) == List and self.head == other.head and self.tail == other.tail

    def __getitem__(self, i):
        return index(i, self)

def isEmpty(l):
    return nil == l

def nonEmpty(l):
    return not isEmpty(l)

def mkList(*xs):
  if xs == ():
    return nil
  else:
    return List(xs[0], mkList(*xs[1:]))

def map(f, l): # {x1, x2, x3, ..., xn} -> {f(x1), f(x2), f(x3), ..., f(xn)}
    if isEmpty(l):
       return nil
    else:
       fx1 = f(l.head)
       t = map(f, l.tail) # f(x1) ** {f(x2), f(x3), ..., f(xn)}
       return List(fx1, t)
