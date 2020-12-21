from Lists import *
from Homework import *
from Sorter import *

class LowWeight:
  def __eq__(self, that):
    return type(that) == LowWeight

  def __str__(self):
      return "L"

lowWeight = LowWeight()

class HeavyWeight:
  def __eq__(self, that):
    return type(that) == HeavyWeight

  def __str__(self):
      return "H"

class Auto:
  def __init__(self, weight, price):
    self.weight = weight
    self.price = price

  def __str__(self):
      return "{" + str(self.weight) + ":" + str(self.price) + "}"


heavyWeight = HeavyWeight()

#L -> LowWeight, H -> HeavyWeight
def parseWeight(str):
  if str == "L":
    return lowWeight
  elif str == "H":
    return heavyWeight
  else:
    return None

#L10000, H44235424, L4234234, ...

def parseAutos(str):
  list = splitString(',', str)
  noSpace = map(deleteWhitespace, list)
  return map(lambda x: Auto(parseWeight(x[0]), int(x[1:])), noSpace)

def sumType(ty, xs):
  if xs == nil:
    return 0
  else:
    if xs.head.weight == ty:
      return xs.head.price + sumType(ty, xs.tail)
    else:
      return sumType(ty, xs.tail)

def countType(ty, xs):
  if xs == nil:
    return 0
  else:
    if xs.head.weight == ty:
      return 1 + countType(ty, xs.tail)
    else:
      return countType(ty, xs.tail)

autos = parseAutos(input())
sumLow = sumType(lowWeight, autos)
sumHeavy = sumType(heavyWeight, autos)
countLow = countType(lowWeight, autos)
countHeavy = countType(heavyWeight, autos)
meanLow = sumLow / countLow
meanHeavy = sumHeavy / countHeavy
print("mean sum low: " + str(meanLow) +
    ", mean sum heavy: " + str(meanHeavy) +
    ", minimum is: " + str(min(meanLow, meanHeavy)))
