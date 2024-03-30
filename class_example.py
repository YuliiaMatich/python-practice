class Student:
  def __init__(self, name, age, grade):
    self.name = name
    self.age = age
    self.grade = grade #0-100

  def get_grade(self):
    return self.grade

class Course:
  def __init__(self, name, max_students):
    self.name = name
    self.max_students = max_students
    self.students = []

  def add_student(self, student):
    if len(self.students) < self.max_students:
      self.students.append(student)
      return True
    return False
  
  def get_average_grade(self):
    pass

s1 = Student("Vasil", 17, 50)
s2 = Student("Tamara", 64, 4)
s3 = Student("Nerd", 12, 100)

course = Course("Tarot_advanced", 2)
course.add_student(s1)
course.add_student(s2)
course.add_student(s3)