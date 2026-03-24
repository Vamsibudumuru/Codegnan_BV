'''string --> string is a collaction of charecters,which represented by ("" or '')
--------->and we can access the using indexing(string can also allow negative indexing)
--------->this is also immutable,where i could not able to modifiy on that particular variables'''

#any = 'python programming'
#print(any)
#print(any[7])
#print(any[7,8,9])#-->TypeError: string indices must be integers, not 'tuple'
#so = any.replace("python","java")
#print(any[7:13])---> slicing
#print(any)
#print(so)
#print(any[-7])
#print(any[20])---->IndexError: string index out of range
'''
day_4 = "I am vamsi from vizag,and i am currently purshuing my betch in anits "
print(f"MY name is {day_4[5:11]}")
print(f"MY btech in {day_4[-6:-1]}")
'''


'''
name = "VAMSI"
print(name[::-1])---> to reverse the string

'''
'''
a_day = "vamsi from vizag"
print(len(a_day))''''''##--------->>>len() method is ued to get char present in the string or find the length of the string

###NOTE:- WE CAN CONVERT A STRING INTO INTEGER IF THE STRING CONTAIN ONLY INTEGER V'''

'''
some = "python is a programming language"
print(some.split(" "))
'''

##
#---------------------------------------------------------------------------------------------------------

#METHOD OF STRINGS

#split()-->remove space , and the is in the list[] it will give the seperated thing in each index


'''some = "python is a programming language"
print(some.split("language"))'''


#syntax---->>>variable_name.split("substring")

#---------------------------------------------------------------------------------------------------------------------
#LOWER()---> THIS IS USED TO CONVERT ALL LETTERS INTO LOWER CASE


'''
some = "python is a PROGRAMMING language"
print(some.lower())
'''
#SYNTAX FOR LOWER ---->variable_name.lower()

#---------------------------------------------------------------------------------------


#upper()------->>> THIS IS USED TO CONVERT ALL LETTERS INTO UPPER  CASE


'''some = "python is a PROGRAMMING language"
print(some.upper())'''


#SYNTAX FOR UPPER ---->variable_name.upper()

#----------------------------------------------

#replace()---->>THIS IS USED TO REPLACE OLD STR WITH THE NEW STR

####SYNATX--->> variable_name.replace("old string","new string")





some = "python is a programming language"
if "yhon" in some:
    print("yes")
else:
    print("NO")























                 
