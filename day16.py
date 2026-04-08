'''Functions()
---->this is block of code which is reuseable.
---->two types 1.Built-in or IN-Build
               2.user define
1.Built in or In-Build
--->they comes with programs and those are already defined...
eg:
--- print(),sum(),map()....
2.User define
---->this created by person who is developing or using for development
NOTE:
--->it's starts with def keyword followed by function name
--->and it has calling function
        eg:
           def func_name(a;b): ---->(a;b)parameters
           ----------
           ----------
           ----------
           fuinction name()--->calling function--(inside functions are arguments)

a = 4
def even(a):
    if a%2==0:
        print("even")
    else:
        print("not even")
even(a)


num = 4
sum=0
def prime_check(num,sum):
    for i in range(1,num+1):
        if num % i ==0:
            sum+=1
    if sum==2:
        print("its a prme")
    else:
        print("not a prime")
    
prime_check(num,sum)

num = 7
n1 = 0
n2 = 1
def fibanacci_check(num,n1,n2):
    for i in range(num+1):
        n3 = n1+n2
        n1 = n2
        n2 = n3
        print(n3)
fibanacci_check(num,n1,n2)        
'''

'''
my_name = "vamsi"
def add(my_name):
    print(my_name)
add(my_name = "budumuru")'''
    


'''
num = 78
sum=0
def prime_check(num,sum):
    for i in range(1,num+1):
        if num % i ==0:
            sum+=1
    if sum==2:
        print("its a prime")
    else:
        print("not a prime")
prime_check(num,sum)    
'''
#default arguements
#it will take the default values from the arguements
'''
def prime_num(num,count):
    for j in range(1,num+1):
        if num % j ==0:
            count+=1
    if count==2:
        print(f"{num}is a prime")
    else:
        print(f"{num} is not a prime")
prime_num(num=9,count=0)
prime_num(num = 47,count = 0)'''

'''
def any(num,num_3,num_2):
    print(f"num = {num},num_2= num_2= {num_2}, num_3= {num_3}")
any(num_2=7, num=0, num_3 = 100)    '''



















