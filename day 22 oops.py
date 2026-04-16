'''
OOPS CONCEPT:-
------------

--->OBJECT-ORIENTED LANGUAGE(OOPS)IS A PROGRAMMING WHERE WE MODEL REAL-WORLD
THINGS ARE OBJECTS THAT CONTAIN BOTH DATA AND FUNCTION(BEHAVIOUR)
-->REUSUABLE OF CODE
-->AND ALSO SCALABLE
-----------------------------------------------------------------------------
'''
#CLASS:- #SYNTAX:- class class_name:
'''
-----

------> CLASS IS A BLUE-PRINT ORT= TEMPLATE THAT DEFINE WHAT KIND OF DATA AND
A BEHAVIOUR A CERTAIN TYPE OF OBJECT WILL HAVE  .

OBJECT:-
------
-->INSTANCE OF CLASS OR AN OBJECT IS A REAL INSTANCE CREATED FROM A CLASS
IT IS ACTUAL THING THAT EXISTS A MEMORY WHILE THE PROGRAM RUNS

'''
#syntax
#                        class car:
#                           pass
#                        car1 = car()---> OBJECT
#                        car2 = car()--->OBJECT


'''
ATTRIBUTES
----------

-->THESE ARE VARIABLES THAT STORE THE DATA RELATED TO A CLASS OR OBJECT
'''
'''
class dog:
    def __init__(self,breed, color):
        self.breed = breed
        self.color = color
dog_1 = dog("golden retriver","brown&blond")
dog_2 = dog("husky","white")
dog_3 = dog("rotweiller","black")
print(dog_3.color)
'''


class car:
    wheels = 4
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
        self.milage = 20
        def drive(self,miles):
            self.milage += miles
            return f"drove{miles} Miles. Total:{self.milage}"
        def info(self):
            return f"{self.make}{self.model}{self.year}"
            car_1 = car("ford","mustang","2008")
            car_2 = car("tayota","camry","2004")
            print(car_1.info())
            print(car_2.info())
            print(car_2.drive(10))

























            











































































