'''
POLYMORPHISM
------------

-->THIS ALLOWS A OBJECT OF DIFFERENT CLASSES TO BE TREATED AS INSTANCE OF THE
SAME BASE CLASS WITH MWETHODS BEHAVING DIFFERENTLY BASED ON THE ACTUAL OBJECT TYPE .
EXAMPLE:-
---------

print(len("python"))
print(len([1,2,3]))


METHOD OVERLOADING
------------------


-->THIS DEFINES MULTIPLE METHODS WITH THE SAME NAME BUT DIFFERENT PARAMETERS
(NUMBER,TYPE, OR ORDER )IN THE CLASS




class calculator():
    def add(self, a, b=0, c=0):
        return a+b+c

cal= calculator()
print(cal.add(2))
print(cal.add(13,4))
print(cal.add(5,17,8))


METHOD OVERRIDING
-----------------

-->THIS OCCURS IN THE CHILD CLASS, REDEFINING A PARENT CLASS METHOD WITH
THE SAME SIGNATURE FOR RUNSIDE.'''
'''
class animal:
    def speak(self):
        return"sound"

class dog(animal):
    def speak(self):
        return"woof"

DOG = dog()
print(DOG.speak())




EXAMPLE
-------

class scolds:
    def speak(self):
        return "sound"

class parent(scolds):  
    def speak(self):
        return "bad*********"

PARENT = parent()
print(PARENT.speak())


OPERATOR OVERLOADING
---------------------

-->THIS IS CUSTOMIZED OPERATOR LIKE +, - FOR USER-DEFINED CLASSES BY
IMPLEMENTING SPECIAL METHODS
EG---__add__ and __sub__


class someone:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
                                    
    def __add__(self, other):
        return someone(self.a + other.a, self.b + other.b, self.c + other.c)

    def __str__(self):
        return f"({self.a}, {self.b}, {self.c})"

any = someone(3, 4, 5)
so = someone(5, 7, 2)
wht = someone(6, 9, 1)

print(any + so + wht)

----------------------------------


DATA ABSTRACTION
----------------

-->THIS HIDES COMPLEX IMPLEMENTATION DETAILS,EXPOSING ONLY ESSENTIAL
FEWATURES VIA ABSTRACT CLASS OR INTERFACE ...


from abc import ABC,abstractmethod
class shape(ABC):
    @abstractmethod
    def area(self):
        pass

class circle(shape):
    def __init__(self,radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius **2
circle = circle(5)
print(circle.area())



'''



























