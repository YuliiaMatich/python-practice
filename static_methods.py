class Math:
  
  @staticmethod #no connection to instanse, used to organize methods under one class
  def add5(x):
    return x + 5
  
  @staticmethod
  def pr():
    print("run")


print(Math.add5(5))
Math.pr()