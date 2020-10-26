from Lists import *
from Maybe import *
from Homework import *

# Со строками можно работать так же как и со списками
def isEmptyStr(a):
    return a == ""

# Со строками можно работать так же как и со списками
def headOfStr(a):
    return a[0]

# Со строками можно работать так же как и со списками
def tailOfStr(a):
    return a[1:]

# Хоть в питоне уже есть встроенная (<) функция для сравнения строк,
# мы все же напишем свою.
def isLessThanStr(a, b):
    if a == "":
       return True if b != "" else False
    else:
       if b == "":
          return False      # "x"    ""
       else:                # "x..." "y..."
          if a[0] < b[0]:   # "b..." "c..."
             return True
          elif a[0] > b[0]: # "c..." "b..."
             return False
          else:             # "b..." "b..."
             return isLessThanStr(a[1:], b[1:])

# print("bgt" < "bgz")
# print(isLessThanStr("bgt", "bgz"))

# print("bgt" < "bg")
# print(isLessThanStr("bgt", "bg"))

# print("bbbbbgt" < "bbbbbgt")
# print(isLessThanStr("bbbbbgt", "bbbbbgt"))

print(sort(isLessThanStr,
           'masha'
        ** 'peter4'
        ** 'peter3'
        ** 'peter2'
        ** 'misha'
        ** 'maria'
        ** 'mark'
        ** 'marat'
        ** 'michael'
        ** nil))
