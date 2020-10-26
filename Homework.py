import sys
from math import floor
import math
from Lists import *
from Maybe import *

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
  if n >= k:
    return n
  else:
    return k

# n, k - целые числа
def min(n, k):
  if k <= n:
    return k
  else:
    return n

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
    if xs == nil:
       return 0
    else:
       return 1 + length(xs.tail)

def fromTo(min, max): # составить список из целых чисел
    if min == max:    # от min (включительно) до max (исключая)
       return nil     # min, min + 1, min + 2, ... max - 1
    else:
       return min ** fromTo(min + 1, max)

def concat(xs, ys):   # сцепить два списка
    if xs == nil:     # concat(1 ** 2 ** nil, 3 ** 4 ** nil) = 1 ** 2 ** 3 ** 4 ** nil
       return ys
    else:
       return xs.head ** concat(xs.tail, ys)

def filter(f, xs):    # составить новый список, в котором находятся все элементы x списка
    if xs == nil:     # xs, такие что f(x) = True
       return nil     # иными словами отфильтровать список xs через функцию f
    else:
       if f(xs.head):
          return xs.head ** filter(f, xs.tail)
       else:
          return filter(f, xs.tail)

def forAll(f, xs) -> bool:
    if xs == nil:     # для всех ли элементов x списка xs выполняется
       return True    # f(x) = True ?
    else:
       return f(xs.head) and forAll(f, xs.tail)

def forSome(f, xs) -> bool:
    if xs == nil:     # Есть ли хотябы один элемент x списка xs
       return False   # такой что f(x) = True ?
    else:
       return f(xs.head) or forSome(f, xs.tail)

def rev(xs) -> List:  # перевернуть список
    if xs == nil:     # rev(True ** 22 ** "ok" ** nil) = "ok" ** 22 ** True ** nil
       return nil
    else:
       return concat(rev(xs.tail), xs.head ** nil)

def span(f, xs) -> (List, List):      # Разделить список xs на пару списков
    if xs == nil:                     # Так что в первом списке пары находятся
       return (nil, nil)              # все первые элементы x списка xs такие что
    else:                             # f(x) = True
       if f(xs.head):                 # а во втором все элементы после первого x
          (l, r) = span(f, xs.tail)   # такого что f(x) = False
          return (xs.head ** l, r)    # включая его самого
       else:                          # Пример: span(lambda x: x % 2 == 0, 2 ** 4 ** 1 ** 6 ** 8 ** 10 ** nil)
          return (nil, xs)            #           == (2 ** 4 ** nil, 1 ** 6 ** 8 ** 10 ** nil)

def split(f, xs) -> (List, List):  # Разделить список xs на пару списков,
    if xs == nil:                  # так что в первом из них хранятся элементы x из xs
       return (nil, nil)           # для которых f(x) = True,
    else:                          # а во втором элементы x для которых f(x) = False
       (left, right) = split(f, xs.tail)
       if f(xs.head):
          return (xs.head ** left, right)
       else:
          return (left, xs.head ** right)

def elemOf(x, xs) -> bool:    # является ли x элементом xs
    if xs == nil:
       return False
    else:
       return x == xs.head or elemOf(x, xs.tail)

def dedupHelper(unique, xs):
    if xs == nil:
       return rev(unique)
    else:
       if elemOf(xs.head, unique):
          return dedupHelper(unique, xs.tail)
       else:
          return dedupHelper(xs.head ** unique, xs.tail)

def dedup(xs) -> List:              # убрать все повторяющиеся элементы
    return dedupHelper(nil, xs)     # xs, при этом сохранив последовательность элементов
                                    # пример: dedup(1 ** 3 ** 1 ** 3 ** 2 ** 1 ** nil)
                                    #           == 1 ** 3 ** 2 ** nil

def find(f, xs):                    # Найти элелемент x в списке xs
    if xs == nil:                   # такой что f(x) = True,
       return nothing               # если такой имеется вернуть его в виде just(x)
    else:                           # (если таких несколько вернуть первый из них),
       if f(xs.head):               # если таковых нет - вернуть nothing
          return just(xs.head)
       else:
          return find(f, xs.tail)

def lookup(n, xs):                  # Имея список xs состоящий из пар значений,
    if xs == nil:                   # найти такую пару (x, y) в нем, что
       return nothing               # x == n.
    else:                           # Если такая есть вернуть just(y)
       (a, b) = n                   # Иначе - вернуть nothing
       if a == xs.head:
          return just(b)
       else:
          return lookup(n, xs.tail)

# Будем говорить, что список xs является множеством или представляет
# собой множество, если в нем нет повторяющихся элементов

def isSet(xs):                      # Является ли xs множеством (проверить нет ли в xs дубликатов)
    return length(xs) == length(dedup(xs))

def union(xs, ys):                  # Вернуть список, который представляет собой множество,
    return dedup(concat(xs, ys))    # полученное в результате операции объединения множеств
                                    # xs и ys

def intersection(xs, ys):                            # Вернуть список, который представляет собой множество,
    return filter(lambda x: elemOf(x, ys), xs)       # полученное в результате операции пересечения множеств
                                                     # xs и ys

def symmetricDifference(xs, ys):
    return filter(lambda u: not elemOf(u, xs) \
                         or not elemOf(u, ys),    # Вернуть список, который представляет собой множество,
                  union(xs, ys))                  # полученное в результате операции симметрической разности множеств
                                                  # xs и ys

# Вернуть список, который представляет собой множество,
# полученное в результате операции разности множеств
# xs и ys
def difference(xs, ys):
    return filter(lambda x: not elemOf(x, ys), xs)

def subsetOf(xs, ys):               # Является ли xs подмножеством ys
    return forAll(lambda x: elemOf(x, ys), xs)

def equalSets(xs, ys):              # Являются ли два множества равными
    return subsetOf(xs, ys) and \
           subsetOf(ys, xs)         # (Проверить, что xs явл подмножеством ys и ys явл подмножеством xs)

# MyBool

# написать класс представляющий собой булево значение True
# (написать __init__, __str__, __eq__)
class MyTrue:
    def __init__(self):
        pass
    def __str__(self):
        return "MyTrue"
    def __eq__(self, other):
        return type(other) == MyTrue

# написать класс представляющий собой булево значение False
# (написать __init__, __str__, __eq__)
class MyFalse:
    def __init__(self):
        pass
    def __str__(self):
        return "MyFalse"
    def __eq__(self, other):
        return type(other) == MyFalse

# Написать функцию которая сопоставляет всроенные булевы значения True/False
# с MyTrue/MyFalse
def fromBool(b):
    if b:
       return MyTrue
    else:
       return MyFalse

# И наоборот
def toBool(myb):
    if myb == MyTrue:
       return True
    else:
       return False

# Создать класс представляющий собой двумерный вектор
# (написать __init__, __str__, __eq__)
class Vec2:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Vec2({self.x}, {self.y})"

    def __eq__(self, other):
        return type(other) == Vec2 \
           and self.x == other.x   \
           and self.y == other.y

    # self < other <=> длина(self) < длина(other) (сравнивать вектора по их евклидовой длине)
    def __lt__(self, other):
        pass # Homework

# Сложить два вектора
def add(a, b):
    return Vec2(a.x + b.x, a.y + b.y)

# Умножить вектор v на число k
def mult(v, k):
    return Vec2(v.x * k, v.y * k)

# Создать список из двух элементов вектора v
def toList(v):
    return v.x ** v.y ** nil

# Если xs имеет длину 2, вернуть вектор из его элементов обернутый в just
# Иначе вернуть nothing
def fromList(xs):
    if length(xs) == 2:
       return just(Vec2(xs[0], xs[1]))
    else:
       return nothing

# Добавить x в отсортированный список xs,
# таким образом, что результат тоже был отсортированным списком.
# Порядок задается бинарной функцией f.
def insertByOrder1(f, xs, x):
    if xs == nil:
       return x ** nil
    else:
       u = xs.head
       if f(u, x):
          return u ** insertByOrder1(f, xs.tail, x)
       else:
          return x ** xs

# Двухстрочный вариант через функцию span
def insertByOrder2(f, xs, x):
    (left, right) = span(lambda u: f(u, x), xs)
    return concat(left, x ** right)

# Вспомогательная функция
def insertionSortHelper(f, xs, sorted):
   if xs == nil:
      return sorted
   else:
      newSorted = insertByOrder1(f, sorted, xs.head)
      return insertionSortHelper(f, xs.tail, newSorted)

# Insertion sort algorithm
def insertionSort(f, xs):
  return insertionSortHelper(f, xs, nil)

# Еще один стандарный алгоритм сортировки списка
def quicksort(f, xs):
  if xs == nil:
    return nil
  else:
    # составить список всех элементов `x` хвоста `xs` для которых выполняется f(x, xs.head)
    # составить список всех элементов `x` хвоста `xs` для которых выполняется not f(x, xs.head)
    # отсортировать оба списка рекурсивно
    # вернуть их конкатенацию вставляя в нее `xs.head` в нужное место
    # Homework
    pass

print(quicksort(lambda x, y: x < y, 1 ** 7 ** 5 ** 1 ** 2 ** 4 ** 9 ** 6 ** nil))

# -------------- ТЕСТЫ -----------------

def checkEqual(str, a, b): # проверка корректности функций
    if a != b:             # печатает ошибку если значения `a` и `b` не равны
       print(str + ": " + f"{a} != {b}", file = sys.stderr)

def test():
    print("<имя>: <получено> != <ожидалось>")
    sys.stdout.flush() # make sure the above line is printed before any test failure
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

    # checkEqual("gcd1", gcd(100, 10), 10)
    # checkEqual("gcd2", gcd(99, 11), 11)
    # checkEqual("gcd3", gcd(45, 25), 5)
    # checkEqual("gcd4", gcd(3, 11), 1)
    # checkEqual("gcd5", gcd(30, 42), 6)

    # checkEqual("gcd6", gcd(-30, 42), -6)
    # checkEqual("gcd7", gcd(-30, -42), 6)

    # checkEqual("lcm1", lcm(5, 3), 15)
    # checkEqual("lcm2", lcm(3 * 5, 5 * 7), 3 * 5 * 7)
    # checkEqual("lcm3", lcm(2 * 3 * 5, 2 * 3 * 7), 2 * 3 * 5 * 7)
    # checkEqual("lcm4", lcm(2 ** 10, 2 ** 9), 2 ** 10)

    # checkEqual("lcm5", lcm(-2, 3), -6)

    # checkEqual("sumRat1", sumRat(1, 4, 7, 8), (9, 8)) # 1/4 + 7/8 = 9/8
    # checkEqual("sumRat2", sumRat(2, 4, 4, 12), (5, 6)) # 2/4 + 4/12 = 5/6
    # checkEqual("sumRat3", sumRat(1, 1, 1, 1), (2, 1)) # 1/1 + 1/1 = 2/1
    # checkEqual("sumRat4", sumRat(0, 99, 4, 7), (4, 7)) # 0/99 + 4/7 = 4/7

    # checkEqual("sqrt1", sqrt(9), (True, 3))
    # checkEqual("sqrt2", sqrt(900 ** 2), (True, 900))
    # checkEqual("sqrt3", sqrt(1), (True, 1))
    # checkEqual("sqrt4", sqrt(0), (True, 0))
    # checkEqual("sqrt5", sqrt(8), (False, ()))

    # checkEqual("solveQuadEq", solveQuadEq(1, 2, 1), (True, (1, -1), (1, -1)))
    # checkEqual("solveQuadEq", solveQuadEq(1, 1, -6), (True, (3, -1), (2, 1)))
    # checkEqual("solveQuadEq", solveQuadEq(3, 3, -18), (True, (3, -1), (2, 1)))
    # checkEqual("solveQuadEq", solveQuadEq(1, 1, 1), (False, ()))
    # checkEqual("solveQuadEq", solveQuadEq(1, -1, 0), (False, ()))

    checkEqual("concat", concat(1 ** 2 ** nil, "1" ** "2" ** nil), 1 ** 2 ** "1" ** "2" ** nil)
    checkEqual("length", length(1 ** 3 ** 5 ** nil), 3)
    checkEqual("fromTo", fromTo(1, 10), 1 ** 2 ** 3 ** 4 ** 5 ** 6 ** 7 ** 8 ** 9 ** nil)
    checkEqual("fromTo", fromTo(1000, 1000), nil)
    checkEqual("filter", filter( lambda x: floor(math.sqrt(x)) * floor(math.sqrt(x)) == x
                               , 1 ** 3 ** 4 ** 9 ** 10 ** nil), 1 ** 4 ** 9 ** nil)
    checkEqual("span", span(lambda x: len(x) == 3,
                            "123" ** "xxx" ** "xx" ** "456" ** "yyy" ** nil),
                      ("123" ** "xxx" ** nil, "xx" ** "456" ** "yyy" ** nil))
    checkEqual("split", split( lambda x: x % 2 != 0
                             , 1 ** 2 ** 3 ** 4 ** 5 ** nil), (1 ** 3 ** 5 ** nil, 2 ** 4 ** nil))
    checkEqual("elemOf", elemOf(0, 1 ** 2 ** 3 ** 4 ** 5 ** nil), False)
    checkEqual("elemOf", elemOf(4, 1 ** 2 ** 3 ** 4 ** 5 ** nil), True)
    checkEqual("rev", rev(1 ** 2 ** 3 ** 4 ** 5 ** nil), 5 ** 4 ** 3 ** 2 ** 1 ** nil)
    checkEqual("dedup", dedup(1 ** 1 ** 1 ** 1 ** nil), 1 ** nil)
    checkEqual("dedup", dedup(1 ** 2 ** 1 ** 3 ** 2 ** 8 ** 1 ** nil), 1 ** 2 ** 3 ** 8 ** nil)

    checkEqual("intersection", intersection(1 ** 2 ** 5 ** 4 ** 8 ** nil, 2 ** 8 ** 1 ** nil), 1 ** 2 ** 8 ** nil)
    checkEqual("intersection", intersection(1 ** 2 ** 5 ** 4 ** 8 ** nil, 7 ** 3 ** 10 ** nil), nil)
    checkEqual("union", union(1 ** 2 ** 5 ** 4 ** 8 ** nil, 7 ** 5 ** 10 ** nil), 1 ** 2 ** 5 ** 4 ** 8 ** 7 ** 10 ** nil)
    checkEqual("isSet", isSet(1 ** 2 ** 5 ** 4 ** 8 ** nil), True)
    checkEqual("isSet", isSet(1 ** 2 ** 2 ** 4 ** 8 ** nil), False)
    checkEqual("subsetOf", subsetOf(1 ** 2 ** 8 ** nil, 1 ** 7 ** 2 ** 8 ** nil), True)
    checkEqual("subsetOf", subsetOf(1 ** 2 ** 8 ** 3 ** nil, 1 ** 7 ** 2 ** 8 ** nil), False)
    checkEqual("difference", difference(1 ** 2 ** 8 ** 3 ** nil, 1 ** 7 ** 2 ** 8 ** nil), 3 ** nil)
    checkEqual("symmetricDifference", symmetricDifference(1 ** 2 ** 8 ** 3 ** nil, 1 ** 7 ** 2 ** 8 ** nil), 3 ** 7 ** nil)
    checkEqual("equalSets", equalSets(1 ** 2 ** 8 ** 3 ** nil, 2 ** 8 ** 1 ** 3 ** nil), True)
    checkEqual("equalSets", equalSets(1 ** 2 ** 8 ** 3 ** nil, 2 ** 8 ** 4 ** 3 ** nil), False)
    checkEqual("Vec2 < Vec2", insertionSort(lambda x, y: x < y, Vec2(3, 4)
                                                             ** Vec2(1, 0)
                                                             ** Vec2(0, 1)
                                                             ** Vec2(8, 15)
                                                             ** Vec2(3, 6)
                                                             ** Vec2(10, 0)
                                                             ** nil),
                                                                Vec2(0, 1)
                                                             ** Vec2(1, 0)
                                                             ** Vec2(3, 4)
                                                             ** Vec2(3, 6)
                                                             ** Vec2(10, 0)
                                                             ** Vec2(8, 15)
                                                             ** nil)
test()
