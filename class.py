class Dog:
  def __init__(self, name):
    self.name = name
    print(name)
    
  def bark(self):
    print("bark")

  def add_one(self, x):
    return x + 1
d = Dog("Tim") ## creating the instanse of class
d.bark()
print(type(d))
print(d.add_one(5))