'''#ENCAPSULATION
-------------
--->THE PRINCIPLE OF BUNDING DATA(ATTRIBUTES) AND METHODS THAT OPERATE ON THAT DATA INTO A SINGLE UNIT, WHICH IS CLASS.
'''

class bankAC:
    def __init__(self,balance):
        self.__balance = balance

    def deposite(self,amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance
Acc = bankAC (15000)
Acc.deposite (7000)
print(Acc.get_balance)
'''
'''
# INHERITANCE--
-------------
---> THIS ALLOWS A CHILD CLSS (SUBCLASS)TO ACQUIRE THE ATTRIBUTE AND METHOD
OF A PARENT CLASS (BASE CLASS) THIS IS CALLED INHERTANCE
1.SINGLE INHERTANCE
2.MULTIPLE
'''
'''


super()
------
--->THIS IS USED TO CALL METHODS OF THE PARENT CLASS FROM THE CHILD CLASS.

class parent:
    def display(self):
        print("This is parent method")

class child(parent):
    def display(self):
        super().display()
        print("This is child method")
obj = child()
obj.display()


class Father:
    def skill_1(self):
        print("Father: hard working")

class Mother:
    def skill_2(self):
        print("Mother: cooking ")

class Child(Father, Mother):
    def All_skills(self):
        print("child: coding")

Any = Child()
Any.skill_1()
Any.skill_2()
Any.All_skills()

















