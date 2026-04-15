#generators
#----------
'''
----> this is a special type of function that return as
ITERATOR which one at a time
----------------------------


YIELD----->it will take a pause and again resume,this is not a nrml keyword can
normal be used in the nrml function
---->this is used to produce a value and pause execution.
----------------------------------------
NEXT()
-----
------>THIS IS USED TO GET NEXT VALUE FROM A GENERATOR
------>WHEN THE VALUE IS FINISHED,IT WILL STOP THE ITERRATOR
'''
def my_generator():
    yield 1
    yield 2
    yield 3
    yield 4

an = my_generator()

print(next(an))
print(next(an))
print(next(an))

def square_gen(n):
    for i in range(n):
        yield i*i
        
for val in square_gen(5):
    print(val)



def square_gen(n):
    for i in range(n):
        yield i+i
        
for val in square_gen(5):
    print(val)























