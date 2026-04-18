'''#constructor(__init__) (first function is constructor)

----------------------
--->a constructor is a special method used to initiallize object data
__init__()
'''
'''
class Student:
    def __init__(self, name, ID, num):
        self.name = name
        self.ID = ID    
        self.num = num  

    def display(self):
        print(self.name, self.ID, self.num)

stu_1 = Student("VAMSI", 103, 9347556969)
stu_1.display()
'''


'''
ACCESS SPECIFIERS
-----------------
1.public
SYNTAX -- name
we can us it anywhere in the problem
2.protected
SYNTAX -- _name
this is only for internal use
3.private
SYNTAX-- __name
this one is restricted

self
----
-->This keyword is instance variable and unique for each object
'''

class some:
    def __init__(self):
        self.public = "public"
        self.protected ="protected"
        self.private = "private"

any = some()
print(any.public)
print(any._protected)
print(any.private)
    
'''self.----> instance variable'''




























