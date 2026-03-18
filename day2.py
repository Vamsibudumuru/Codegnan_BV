'''
variables--> variables are named storage location that is usedn tohold the data
in the memory to make it simple it is the label which points out toa value-->storage placeholders

RULES FOR DEFINING VARIABLES
-->A-Z,a-z,0-9
-->starts with uppercase, lowercase letters,even with a underscore_
-->but you cannot start with symbols(@'#,$...),even number also

better preferable way is go with general purpose -->you to store your details name,email_id,account_number...


'''
a=1
b=33
c=34
#python is dynamically typed ,you need not to define the datatype and also
#only the recent value to the variable with the same name is poiunted

print (a)
print(c)

#1a23=34 #syntax error

#@werf =4.5 #syntax error

#$dsf =12 #syantax invalid

## store your personal details

name = "codegnan"
Location = "vizag"
Age = 21
emailid = "cmo@gmail.com"
email_id ="cmo@gmail.com"
print(name,Location,Age,email_id)

#HOW TO ASSIGN MULTIPLE VALUES TO A VARIABLES
akash,vamsi,ravi,sunny,deekshith=21,20,23,24,25
print(akash)
print(vamsi)
print(ravi)
print(sunny)
print(deekshith)

#assign same values to multiple variables

x=y=z=12
print(x,y,z)

#keywords are reserved word which will have specific usuage
#there are 35 keywords in python
#never use keywords as identifiers

#if=23
#lambda = 'vamsi'
#false =0 cannot assign

#python is case-sensitive
false=25
#identifiers are names given to variables,functions,classes,objects...
#literals are fixed values to a identifiers
name=25

#name is identifier ,25 is literal
#single line  comments -->#
#multiple line comments--> '''start'''

#BUILT-IN DATATYPES -->NUMERIC,BOOLEAN,COLLECTION

#NUMERIC DATATYPES-->INT,FLOAT,COMPLEX
#int--> count,values,quantities
#float--> temperatue,percentage,price
#complex --> specific covrsation (real and imaginary)

count=456
print(count)
print(type(count))

price = 145.45
print(price)
print(type(price))

j3 =26
value=4+j3
print(value)
print(type(value))


###TYPECASTING --> CONVERTING ONE TYPE TO ANOTHER

###int -->float, complex

'''age = 34
print(type(age))

b = float(age)
print(b)
print(type(b))
c = complex(age)
print(c)
print(type(c))'''

#FLOAT, COMPLEX


#BOOLEAN DATATYPES -->VALIDATION-->TRUE/FALSE

'''a = True
print(a)
print(type(a))

#typeconversion of bool
b = int(a)
print(b)
c = float(a)
print(c)
d = complex(float(int(False)))
print(d)
print(type(d))'''


#INPUT-->input()/output-->print()
'''
a=5
print(a)

a=input("enter the value")#any input but as str
print(a)
print(type(a))


a=int(input("enter the value"))#only integer input
print(a)
print(type(a))

b = float(input("enter another value"))
print(b)
print(type((b)'''


######### now let us work on a simple case study using above-->

#### details of the student
name = input("enter the student name:")
print("-------------------------------")
admission_fees = int(input("Enter the admission Fees:"))
tution_fees = float(input("Enter the Tution fees:"))
hostel_fees=float(input("Enter the hostel fees:"))
#####calculate the total fee
total_fees = admission_fees + tution_fees + hostel_fees
print("----------------------------------------")
print("student Name :",name)
print("Admission fees is :",admission_fees)
print("Tution fees is:",tution_fees)
print("hostel fees is :",hostel_fees)
print("-------------------")






























