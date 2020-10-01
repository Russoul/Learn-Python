from Homework import *
from Lists import *

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
