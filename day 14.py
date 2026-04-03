'''num = int(input("enter the limit:"))
for j in range (num):
    for i in range (j) :
        print("*",end = "")
    print()
'''    
####----------pattern printing-----------


'''
num = int(input("enter the limit:"))
for j in range (num):
    for i in range (j) :
        print(i,end = "")
    print()
'''
    
'''    
0
01
012
0123
'''
#----------number printing---------------------
'''
num = int(input("enter the limit:"))
for j in range (1,num+1):
    for j in range (num+1) :
        print("*",end = "")
    print()
'''
'''
*******
*******
*******
*******
*******
*******
'''
    
#----------square printing---------------------
    
'''
num = int(input("enter the limit:"))
for j in range (num):
    for i in range (num-j) :
        print("**",end = "")
    print()
'''


'''
****************
**************
************
**********
********
******
****
**
'''


#------------reverse star printing----------   

'''
num = int(input("enter the limit:"))
for i in range (1,num+1):
    for j in range (1,i+1):
        print("*",end = "")
    print()
'''
'''
*
**
***
****
*****
******
*******
'''
    

#-----------triangle printing--------------

'''
num = int(input("enter the limit: "))
for j in range (num):
    print(" " *(num-j),end ="")
    for i in range (j+1):
        print("*",end=" ")
    print()
'''
'''
      * 
     * * 
    * * * 
   * * * * 
  * * * * * 
 * * * * * * 
'''
#------------remove space triangle-------------
'''
num = int(input("enter the limit: "))
for j in range (num):
    print(" " *(num-j),end ="")
    for i in range (j+1):
        print("*",end="")
    print()
'''

'''
         *
        **
       ***
      ****
     *****
    ******
   *******
  ********
 *********

'''


