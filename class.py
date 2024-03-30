class Dog:
  def __init__(self, name, age): ## runs every time the instanse of class is created
    self.name = name
    self.age = age
    print(name)

  def bark(self):
    print("bark")

  def get_name(self):
    return self.name
  
  def add_one(self, x):
    return x + 1
  
  def set_age(self, age):
    self.age = age

  def get_age(self):
    return self.age
  
d = Dog("Tim", 12) ## creating the instanse of class
d.set_age(23)
d.bark()
print(type(d))
print(d.add_one(5))
print(d.get_name())
print(d.get_age())