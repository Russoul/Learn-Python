from __future__ import annotations
from typing import *
A = TypeVar('A')

class Nil:
    def __rmul__(self : Nil, other : A) -> List:
        return List(other, self)

    def __rpow__(self : Nil, other : A) -> List:
        return List(other, self)

    def __eq__(self, other):
        return type(other) == Nil or other == [] or other == ()

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


class List:
    def __init__(self : List, x : A, xs : List):
        self.head = x
        self.tail = xs

    def __eq__(self : List, other : List) -> bool:
        pass

    def __rpow__(self : List, other : A) -> List:
        return List(other, self)

    def __str__(self : List) -> str:
        return showList(self)

    def __eq__(self : List, other : List):
        return type(other) == List and self.head == other.head and self.tail == other.tail

def isEmpty(l):
    return nil == l

def nonEmpty(l):
    return not isEmpty(l)

l = 1 ** 2 ** 3 ** nil
r = 0 ** 2 ** 3 ** nil

print(l)
print(r)
print(l.tail == r.tail)
print(isEmpty([]))
print(isEmpty(()))
print(isEmpty(nil))
print(nonEmpty(1 ** nil))
