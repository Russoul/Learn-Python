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
def splitString(delim, str, store = ''):
  if str == '':
     return store ** nil
  elif str[0] != delim:
     return splitString(delim, str[1:], store + str[0])
  else:
     return store ** splitString(delim, str[1:], '')

# Берет список строк и соединяет их в одну строку,
# соединяя их символом '\n'
def joinListOfStrs(xs):
  if xs == nil:
    return ''
  else:
    return xs.head + '\n' + joinListOfStrs(xs.tail)

# Homework (1)
def InitialiseA():
    x = input()
    v = splitString(' ', x)
    print(v)
    a = v[0].x
    b = v[1].x
    c = v[2].x
    print(b[0] + ". " + c[0] + ". " + a)

# Homework (2)
def InitialiseB():
  x = input()
  v = splitString('/', x)
  map(print, v)
# InitialiseB()

# ПРОЧИТАЙ МЕНЯ !
# Чтобы дальнейший код работал, нужно создать два файла:
# input.txt и output.txt в той же папке что и этот проект
# В input.txt поместить любой текст

# Говорим питону с каким файлом мы собираемся работать и
# в каком режиме ('r' - чтение, 'w' - перезапись, 'a' - добавление (запись сверху), ...)
inputFile = open('input.txt', 'r')

# Считываем весь файл в виде одной строки
lines = inputFile.read()

# Закрываем этот файл (более он нам не нужен в питоне)
inputFile.close()

# Превращаем эту строку в список отображаемых строк
linesList = init(splitString('\n', lines))

# Сортируем
sortedList = quicksort(isLessThanStr, linesList)

# Открываем файл в который перезапишем отсортированный ввод
outputFile = open('output.txt', 'w')

# (Пере)записываем
outputFile.write(joinListOfStrs(sortedList))

# Закрываем файл
outputFile.close()

# ДЗ:
# Поменять программу так, чтобы из одного файла считывался список (построчно)
# чисел. Далее над этим списком производились следущие действия
#  (каждое действие производится вне зависимости от остальльных над изначальным списком):
# 1) считалась их сумма (сумма чисел)
# 2) находился минимальный элемент списка, как число
# 3) находился минимальный элемент списка, как строка:
#    то есть нужно найти минимальную строку используя лексикографическое
#    сравнение строк списка.

# Результат каждой операции нужно записать во второй файл
