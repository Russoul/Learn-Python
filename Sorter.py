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

# Делим строку на список из линий (отображаемых строк)
def splitString(str, store = ''):
  if str == '':
     return nil
  elif str[0] != '\n':
     return splitString(str[1:], store + str[0])
  else:
     return store ** splitString(str[1:], '')

# "Открываем" файл 'new.txt' в режиме чтения 'r'
# Дальнейшие действия с файлом возможны через переменную `f`
# Не забудь создать этот файл перед запуском
inputFile = open('new.txt', 'r')

# Считываем весь файл в виде одной строки
lines = inputFile.read()

# превращаем эту строку в список отображаемых строк
linesList = splitString(lines)

# TODO Homework отсортировать полученный список любым методом,
# и записать его в какой либо другой файл
# (для этого нужно открыть этот файл в режиме записи 'w') и использовать функцию его класса `write`
# пример:

#outputFile = open('output.txt', 'w')
#outputFile.write(yourStringHere)
