from Lists import *
from Maybe import *

class Cat:
   def __init__(self, n, a):
       self.name = n
       self.age = a

   def __eq__(self, other):
       return type(other) == Cat and self.name == other.name and self.age == other.age

class Dog:
  def __init__(self, name, age, eyeColor):
      self.properties = name ** age ** eyeColor ** nil

  def name(self):
      return self.properties.head

  def age(self):
      return self.properties.tail.head

  def eyeColor(self):
      return self.properties.tail.tail.head

  def __eq__(self, other):
      return type(other) == Dog and self.properties == other.properties

  def __str__(self):
      return "Dog(" + self.name() + ", " + str(self.age()) + ", " + self.eyeColor() + ")"

a = Cat("name", 18)
b = Cat("name", 18)

print(a == b)

dog1 = Dog("dog", 18, "green")
dog2 = Dog("dog", 18, "green")

def strPair(pair):
    (a, b) = pair
    return "(" + str(a) + ", " + str(b) + ")"

print(dog1 == dog2)
print(dog1.name())
print(strPair((dog1, dog2)))
