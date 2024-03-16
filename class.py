class Dog:
  def bark(self):
    print("bark")

  def add_one(self, x):
    return x + 1
d = Dog() ## creating the instanse of class
d.bark()
print(type(d))
print(d.add_one(5))