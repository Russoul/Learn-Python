from __future__ import annotations
from typing import *
from Homework import *

class Nil:
    def __rpow__(self, other):
        return List(other, self)

    def __eq__(self, other):
        return type(other) == Nil

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
    def __init__(self, x, xs):
        self.head = x
        self.tail = xs

    def __rpow__(self, other):
        return List(other, self)

    def __str__(self):
        return showList(self)

    def __eq__(self, other):
        return type(other) == List and self.head == other.head and self.tail == other.tail

def isEmpty(l):
    return nil == l

def nonEmpty(l):
    return not isEmpty(l)

def map(f, l): # {x1, x2, x3, ..., xn} -> {f(x1), f(x2), f(x3), ..., f(xn)}
    if isEmpty(l):
       return nil
    else:
       fx1 = f(l.head)
       t = map(f, l.tail) # f(x1) ** {f(x2), f(x3), ..., f(xn)}
       return fx1 ** t



l = 1 ** 2 ** 3 ** nil
r = 0 ** 2 ** 3 ** nil

print(l)
print(r)
print(l.tail == r.tail)
print(isEmpty([]))
print(isEmpty(()))
print(isEmpty(nil))
print(nonEmpty(1 ** nil))

t = 1 ** 2 ** 3 ** nil
print(t, ":", map(lambda x: (x + 1) ** 2, t))

print("-- ПРОВЕРКА НА ПАЛИНДРОМНОСТЬ --")

def checkPalindromes(l):
    map(lambda x: print(str(x) + ":" + str(isPalindrome(x))), l)


checkPalindromes(111 ** 1 ** 123321 ** 123 ** 12000021 ** nil)
