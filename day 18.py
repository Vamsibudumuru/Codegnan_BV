'''#lambda functions----
#-------------------
------> this is also called function
-----> a lambda function can take n number of arguements but have only one
expression

syntax
-----
lambda(keyword)arguements : expression'''
'''
any = lambda so: so + 10
print(any(6))

some = lambda an, how, do :(how - an)* do
print(some(40,99,12))
'''


#another problem


'''
any = lambda so: so * 10
print(any(6))

some = lambda an, how, do :(how + an)+ do
print(some(40,99,12))
'''


#listcomprehension:
'''------------------
--->this is offee the shortest syntax when you want to create a new list
from the list exiting list


syntax
--------
3              variables_name =[expression loop and condition]'''

old_list = [1,2,3,4,5,6]
new_list = [j for j in old_list if j%2==0]
print(new_list)




































