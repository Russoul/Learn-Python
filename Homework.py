import sys
from Lists import *

# --------- Booleans and Numbers ----------

# x is Bool, y is Bool
def xor(x, y): # x ^ y ("исключающее или", одна из 16 булевых функций 2-х аргументов)
    if x:
       if y:
          return False
       else:
          return True
    else:
       if y:
          return True
       else:
          return False

# n >= 0
def numOfDigits(n): # количество цифр в числе
    if n // 10 == 0:
       return 1
    else:
       return 1 + numOfDigits(n // 10)

# n >= 0
def sumOfDigits(n): # сумма цифр в числе
    if n // 10 == 0:
       return n
    else:
       return n % 10 + sumOfDigits(n // 10)

# n >= 0
def maxDigit(n): # максимальная цифра в числе
    if n // 10 == 0:
       return n
    else:
       m = maxDigit(n // 10)
       if m > n % 10:
          return m
       else:
          return n % 10

# d >= 0, ds >= 0
def join(d, ds): # добавить число `d` к числу `ds` спереди
    if ds // 10 == 0:
       return 10 * d + ds
    else:
       r = join(d, ds // 10)
       return 10 * r + ds % 10

def reverse(n):  # перевернуть число
    if n // 10 == 0:
       return n
    else:
       r = reverse(n // 10)
       dif = numOfDigits(n // 10) - numOfDigits(r)
       return join(n % 10 * 10 ** dif, r)

# n >= 0
def isPalindrome(n): # является ли `n` палиндромом
    return n == reverse(n)

# n, k - целые числа
def max(n, k):
    pass # Homework

# n, k - целые числа
def min(n, k):
    pass # Homework

def sgn(n): # "знак" числа (или 0)
    if n > 0:
       return 1
    elif n < 0:
       return -1
    else:
       return 0

def abs(n): # модуль числа
    if n >= 0:
       return n
    else:
       return -n

# n > 0, k > 0, n = max(n, k), k = min(n, k)
def gcdHelper(n, k): # используй рекурсию
    return 1         # Homework

# n =/= 0, k =/= 0, n, k - целые числа
def gcd(n, k): # наибольший общий делитель
    return sgn(n * k) * gcdHelper(max(abs(n), abs(k)), min(abs(n), abs(k)))

# n =/= 0, k =/= 0, n, k - целые числа
def lcm(n, k):    # наименьшее общее кратное
    g = gcd(n, k) # Homework
    pass

# b =/= 0, d =/= 0, a, b, c, d - целые числа
def sumRat(a, b, c, d): # Найти a/b + c/d
    pass                # возвратить отдельно числетиль
                        # и знаменатель результата
                        # результат должен быть в
                        # сокращенном виде
                        # Homework

# n >= 0, k = 0, 1, 2, 3, ...
def sqrtHelper(n, k):   # Homework
    pass                # используй рекурсию

# n >= 0
def sqrt(n): # найти целый квадратный корень натурального числа
             # если такой есть
    return sqrtHelper(n, 0)

# a =/= 0, a, b, c - целые числа
def solveQuadEq(a, b, c): # Решить a * x ** 2 + b * x + c = 0
    pass                  # в случае если есть целые корни


# -------- Lists ---------

def length(xs): # посчитать длину списка
    pass

def fromTo(min, max): # составить список из целых чисел
                      # от min (включительно) до max (исключая)
    pass              # min, min + 1, min + 2, ... max - 1

def concat(xs, ys):   # сцепить два списка
    pass              # concat(1 ** 2 ** nil, 3 ** 4 ** nil) = 1 ** 2 ** 3 ** 4 ** nil

def filter(f, xs):    # составить новый список, в котором находятся все элементы x списка
    pass              # xs, такие что f(x) = True
                      # иными словами отфильтровать список xs через функцию f

def forAll(f, xs) -> Bool:
    pass              # для всех ли элементов x списка xs выполняется
                      # f(x) = True ?

def forSome(f, xs) -> Bool:
    pass              # Есть ли хотябы один элемент x списка xs
                      # такой что f(x) = True ?

def rev(xs):          # перевернуть список
    pass              # rev(True ** 22 ** "ok" ** nil) = "ok" ** 22 ** True ** nil

def span(f, xs):      # Позже
    pass

def split(f, xs):     # Позже
    pass

def find(f, xs):      # Позже
    pass

def lookup(n, xs):    # Позже
    pass

# -------------- ТЕСТЫ -----------------

def checkEqual(str, a, b): # проверка правильности функций
    if a != b:             # печатает ошибку если значения `a` и `b` не равны
       print(str + ": " + f"{a} != {b}", file = sys.stderr)

def test():
    checkEqual("xor00", xor(0, 0), 0)
    checkEqual("xor10", xor(1, 0), 1)
    checkEqual("xor01", xor(0, 1), 1)
    checkEqual("xor11", xor(1, 1), 0)

    checkEqual("numOfDigits1", numOfDigits(123), 3)
    checkEqual("numOfDigits2", numOfDigits(2), 1)

    checkEqual("sumOfDigits1", sumOfDigits(12345), 15)
    checkEqual("sumOfDigits2", sumOfDigits(1), 1)
    checkEqual("sumOfDigits3", sumOfDigits(102), 3)

    checkEqual("maxDigit1", maxDigit(12345), 5)
    checkEqual("maxDigit2", maxDigit(1), 1)
    checkEqual("maxDigit3", maxDigit(100992), 9)

    checkEqual("join1", join(1, 0), 10)
    checkEqual("join2", join(1, 2), 12)
    checkEqual("join3", join(1, 234), 1234)
    checkEqual("join4", join(0, 2345), 2345)
    checkEqual("join5", join(3, 180), 3180)

    checkEqual("join6", join(32, 180), 32180)
    checkEqual("join7", join(120, 3450), 1203450)

    checkEqual("reverse1", reverse(123), 321)
    checkEqual("reverse2", reverse(20), 2)
    checkEqual("reverse3", reverse(123400), 4321)
    checkEqual("reverse4", reverse(1800300), 30081)
    checkEqual("reverse5", reverse(1020030004), 4000300201)

    checkEqual("isPalindrome1", isPalindrome(5), True)
    checkEqual("isPalindrome2", isPalindrome(101), True)
    checkEqual("isPalindrome3", isPalindrome(1101), False)
    checkEqual("isPalindrome4", isPalindrome(2110112), True)
    checkEqual("isPalindrome5", isPalindrome(123321), True)
    checkEqual("isPalindrome6", isPalindrome(2001010101002), True)
    checkEqual("isPalindrome7", isPalindrome(201010101002), False)
    checkEqual("isPalindrome8", isPalindrome(200110101002), False)

    checkEqual("gcd1", gcd(100, 10), 10)
    checkEqual("gcd2", gcd(99, 11), 11)
    checkEqual("gcd3", gcd(45, 25), 5)
    checkEqual("gcd4", gcd(3, 11), 1)
    checkEqual("gcd5", gcd(30, 42), 6)

    checkEqual("gcd6", gcd(-30, 42), -6)
    checkEqual("gcd7", gcd(-30, -42), 6)

    checkEqual("lcm1", lcm(5, 3), 15)
    checkEqual("lcm2", lcm(3 * 5, 5 * 7), 3 * 5 * 7)
    checkEqual("lcm3", lcm(2 * 3 * 5, 2 * 3 * 7), 2 * 3 * 5 * 7)
    checkEqual("lcm4", lcm(2 ** 10, 2 ** 9), 2 ** 10)

    checkEqual("lcm5", lcm(-2, 3), -6)

    checkEqual("sumRat1", sumRat(1, 4, 7, 8), (9, 8)) # 1/4 + 7/8 = 9/8
    checkEqual("sumRat2", sumRat(2, 4, 4, 12), (5, 6)) # 2/4 + 4/12 = 5/6
    checkEqual("sumRat3", sumRat(1, 1, 1, 1), (2, 1)) # 1/1 + 1/1 = 2/1
    checkEqual("sumRat4", sumRat(0, 99, 4, 7), (4, 7)) # 0/99 + 4/7 = 4/7

    checkEqual("sqrt1", sqrt(9), (True, 3))
    checkEqual("sqrt2", sqrt(900 ** 2), (True, 900))
    checkEqual("sqrt3", sqrt(1), (True, 1))
    checkEqual("sqrt4", sqrt(0), (True, 0))
    checkEqual("sqrt5", sqrt(8), (False, ()))

    checkEqual("solveQuadEq", solveQuadEq(1, 2, 1), (True, (1, -1), (1, -1)))
    checkEqual("solveQuadEq", solveQuadEq(1, 1, -6), (True, (3, -1), (2, 1)))
    checkEqual("solveQuadEq", solveQuadEq(3, 3, -18), (True, (3, -1), (2, 1)))
    checkEqual("solveQuadEq", solveQuadEq(1, 1, 1), (False, ()))
    checkEqual("solveQuadEq", solveQuadEq(1, -1, 0), (False, ()))

    checkEqual("concat", concat(1 ** 2 ** nil, "1" ** "2" ** nil), 1 ** 2 ** "1" ** "2" ** nil)

test()
