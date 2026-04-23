class User:
    def __init__(self, name, age, university_depart):
        self.name = name
        self.age = age
        self.main_depart = university_depart

    def display(self):
        print(f"Name : {self.name}")
        print(f"Age : {self.age}")
        print(f"Main_course : {self.main_depart}")


class Student(User):
    def __init__(self, name, age, university_depart):
        super().__init__(name, age, university_depart)
        self.courses = []

    def enroll_course(self, course):
        self.courses.append(course)
        print(f"{self.name} is enrolled in {course}")

    def view_courses(self):
        print(f"{self.name}'s courses : ")
        for c in self.courses:
            print("-", c)


name = input("Enter student name: ")
age = int(input("Enter age: "))
dept = input("Enter university department: ")
university_name = input("Enter university name:")
s1 = Student(name, age, dept)

s1.display()

n = int(input("How many courses to enroll? "))

for i in range(n):
    course = input(f"Enter course {i+1}: ")
    s1.enroll_course(course)

s1.view_courses()
