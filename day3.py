#operators
#different types of  operators
#conditional sTATEMENTS-->"""""""if,elif,else,nested if""""


'''
operators--> an operator is an symbol that performs an operation on one or
more values(operands)and produces a result

operators are primarily used :
--> calculate values
-->compare values/ input
--> make a decisions
--> control the program flow

THERE ARE 7 MAJOR CATEGORIES OF OPERATORS IN PYTHON

------>>>>ARTHIMETIC OPERATORS
------>>>>ASSIGNMENT OPERATORS
------>>>>COMPARISION OPERATORS
------>>>>MEMBERSHIP OPERATORS(IN ,NOT IN)
---->>>>IDENTITY OPERATOR(IS ,ISNOT)
----->>>>BITWISE OPERATOR
------>>>>LOGICAL OPERATOR(AND, OR, NOT)

'''
#Arthimetic operators-->arthimetic operators perform mathematicaloperators

###   + -->addition

###   - -->subtraction

###   * -->multiplication

###   / --> divisoion


##  ** --> Exponenet

##  % -->modulus

###  // --> integer division


'''
a = 5
b = 3
print(a+b)
print(a-b)
print(a*b)
print(a/b)#return the result in float values
print(a**b)#return the exponential value
print(a%b)#modulus division -->returns remaoinder
print(a//b)#flooring / Integer division --> returns quotient discards
'''

###f-string notation'''
'''
num1 = int(input("enter the first value:"))
num2 = int(input("enter the second value:"))
result = (num1 + num2)*4
print("The result is",result) ###standard notation


#####   f-string noptation
print(f'The result is {result}')
print(f'The result of {num1} and {num2} is {result},{num1*num2},{num1/num2}')

'''
#assignment operators
#--> = assign, +=assign, +=addition assignment,
#--> subtract assignment,*=,/=,//=,**/*=

#they are majorly used for code reptition in application usuage
'''
a = 5
b = 7
a += 3 ##--> a = a+2
print(a)
b += a
print(b)

## in similar way check for -=, *=, **=, /=, %=, //=

b -= 3 #b= b-3
print(b)
print(f'the updated values of a and b are {a} and {b}')
b *=a
print(b)
'''

#RELATIONAL OR COMPARISION OPERATORS-->THEY ALWAYS RETURN THE BOOLEAN
#VALUES (TRUE/FALSE)


##== IS EQUAL TO, != NOT EQUAL TO
#< LESS THAN, > GREATER THAN, >=, <=\
'''
a = int(input("enter a value:"))
b = int(input("enter another value:"))
print(a==b)
print(a!=b)
print(a<b)
print(a>b)
print(a<=b)
print(a>=b)'''

### MEMEBERSHIP OPERATOR --> THEY CHECK FOR THE EXISTENCE OF AN OBJECT IN A
#COLLECTOIN--> IN, NOTIN
'''
a = "visakhapatnam"
print(type(a))
print('k' in a)
print('V' in a)
print('D'in 'vamsi')
print('v' not in 'vamsi')


b = [12,56,67,78,97]
c = int(input("Enter the value:-"))
print(c)
print(c in b)
print(c  not in b)
'''
#LOGICAL OPERATORS -->THEY ARE USED TO COMBINE MULTIPLE CONDDITIONS
## AND OR NOT
'''
age = int(input("ENTER THE AGE:"))
vote_right = True
print (age>=18 and vote_right)
print(age<=18 or vote_right)
print(not vote_right)'''

### (id) FUNCTION IT IS DIFFERENT FROM == OPERATION -> IS, ISNOT

'''
a = [1,3,4,5]
b = [1,3,4,5]
print(a==b)
print(id(a))
print(id(b))
print( a is b)
print(a is not b)

c = b
print(c)
print(id(c))
print(c is b)
'''
#BITWISE OPERATORS -->BITWISE AND & ,BITWISE OR |PERFORM BITWISE OPERATOR
#WE GET THE RESULT(REMEMBER THE BINARY CONVERSATION)
print(5&3)
print(bin(5)) #return binary number



###### TASK --->>>>> NOW YOU HAVE ALL OPERATORS CREATE A CHECKER TASK
#git add .#
#git coomit -m "operators usuage"
#gitpush-u origin main





































