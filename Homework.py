import sys


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
    pass         # используй рекурсию
                 # Homework

# 0 <= d <= 9, ds >= 0
def join(d, ds): # добавить цифру `d` к числу `ds` спереди
    pass         # используй рекурсию
                 # Homework

# n >= 0
def reverse(n):  # перевернуть число, используй рекурсию
    pass         # используй вспомогательную функцию `join`
                 # Homework

# n >= 0, rn = reverse(n)
def isPalindromeHelper(n, rn): # вспомогательная функция
    pass                       # используй рекурсию
                               # Homework

# n >= 0
def isPalindrome(n): # является ли `n` палиндромом
    return isPalindromeHelper(n, reverse(n))

# -------------- ТЕСТЫ -----------------

def checkEqual(str, a, b): # проверка правильности функций
    if a != b:             # печатает ошибку если значения `a` и `b` не равны
       print(str + ": " + f"{a} != {b}", file = sys.stderr)

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
