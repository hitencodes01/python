class Student:

    num_student = 0
    passing_year = 2025

    def __init__(self,name,rollno):
        self.name = name
        self.rollno = rollno
        Student.num_student += 1

std1 = Student("hiten",1)
std2 = Student("rohit",2)
std3 = Student("saurabh",3)
std4 = Student("harsh",4)
print(f"my class of session {Student.passing_year} has following {Student.num_student} student")
print(std1.name)
print(std2.name)
print(std3.name)
print(std4.name)




