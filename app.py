# basic inputs and datatypes
name = input("Whats your name? ")
birth_year = input("Enter your birth year: ")
age = 2024 - int(birth_year)
print("Hello " + name + " your age is " + str(age))

# basic sum calc
first_number = input("First: ")
second_number = input("Second: ")
Sum = float(first_number) + float(second_number)
print("Sum: " + str(Sum));

# strings finding index or -1 and replace
course = "Python for beginners"
print(course.find("on"))
print(course.replace("Py", "My"))
print("for" in course)

# math
# // returns integer, / returns floating
print(10 // 3)
price = 25
print(price > 10 and price < 25)
print(price > 10 or price < 30)
print(not price > 10)

# if
temperature = 35
if temperature > 30:
  print("It's a hot day")
elif temperature > 20:
  print("It's a nice day")
else:
  print("It's cold")

