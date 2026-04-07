'''#dict. is a method which have  the key values in order

#ex: "name":,"vamsi"



#and op. both stst must me true or flase

#or op. eithr 1 statement must be true


#range() it is mainly used in loops to identify the sequence of integers in iteraton
'''





 #FEBNOCCI



num = int(input("enter a number:"))
sum = 5
n1 = 0
n2 = 1
for i in range(num+1):
    n3 = n2+n1
    n2 = n3
    n3 = n1
    print(n3)
