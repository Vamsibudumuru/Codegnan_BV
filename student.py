
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_basic_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")

class Student(Person):
    def __init__(self, name, age, student_id, course):
        super().__init__(name, age)
        self.student_id = student_id
        self.course = course

    def display_details(self):
        print("\n--- Student Details ---")
        self.display_basic_info()
        print(f"Student ID: {self.student_id}")
        print(f"Course: {self.course}")


class Professor(Person):
    def __init__(self, name, age, employee_id, department):
        super().__init__(name, age)
        self.employee_id = employee_id
        self.department = department

    def display_details(self):
        print("\n--- Professor Details ---")
        self.display_basic_info()
        print(f"Employee ID: {self.employee_id}")
        print(f"Department: {self.department}")


student1 = Student("VAMSI", 20, "A22126511182", "INFORMATION TECHNOLOGY")
professor1 = Professor("G.BHANU TEJA", 27, "PFS", "VIZAG CODEGNAN")
student2 = Student("DEEKSHITH",21, "A22126511188","CYBER SECURITY")
professor2 = Professor("MALLI",27, "JFS", "VIZAG CODEGNAN")

student1.display_details()
professor1.display_details()
student2.display_details()
professor2.display_details()

