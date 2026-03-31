'''any_ = "python is a programming language"
vowel_cou = 0
space_cou = 0
con_cou = 0
for j in any_:
    if j in "AEIOUaeiou":
        vowel_cou += 1
    elif j == " ":
        space_cou += 1
    else:
        con_cou += 1
print(vowel_cou)
print(space_cou)
print(con_cou)


any_ = "python is a programming language"
vowel_cou = 0
space_cou = 0
con_cou = 0
for j in any_:
    if j in "AEIOUaeiou":
        vowel_cou += 1
    elif j == " ":
        space_cou += 1
print(f"this is count of all vowel in the string {vowel_cou}")
print(f"this is the count of all space in the string {space_cou}")
print(f"this is the count of all cons_ in the string {len(any_)-(vowel_cou + space_cou)}")


a = 9
print(a)
for j in range(1,10):
    print(j)

#range()----->this is used to generate number
#SYNTAX:range(start,end,step)

for j in range(1,10,30):
    print(j)

any = "123"
print(int(any))
print(list(any))
print(tuple(any))

so = 123
print(str(so))
print(float(123))

an = [1,2,3]
vs = str(an)
print(type(vs))
print(tuple[vs])

a =[(1,2),(3,4)]
print(dict(a))

rev_str = "vamsi"
print(rev_str[::-1])


rev_str = "vamsi"
empty_ = ""
for j in rev_str:
    empty_ = j + empty_#(we have to reverse the name )logic
    print(empty_)



rev_str = "non"
empty_ = ""
for j in rev_str:
    empty_ = j + empty_
    print(empty_)
if empty_ == rev_str:
    print(f"{rev_str} is pallindrome")
else:
    print(f"{rev_str} is not a pallindrome")'''

'''
for num in range(1,100):
    if num % 2 == 0:
        print(f"{num}is even number")
    else:
        print(f"{num}is odd number")'''
