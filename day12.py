'''table_num = 8
for j in range(1,50):
    print(f"{table_num} X {j} = {table_num * j}")'''
'''
an="python is a programming language"
count_U=0
count_L=0
for ch in an :
    if ch.isupper():
        count_U += 1
    elif ch.islower () :
        count_L += 1
print(f"there are total (count_U) cap L")
print(f"there are total (count_L) small L")'''

'''
an = "python is a programming language"
Cap_l = []
small_l = []
for ch in an:
      if ch.isupper():
            Cap_l.append(ch)
      elif ch.islower():
             small_l.append(ch)
print(f"{Cap_l} contain all cap l")
print(f"{small_l} contain all small l")
'''

'''
SBI_VAMSI_BUDUMURU_AC_DETAILS ={"NAME": "vamsi",
                                "ATM PIN": "9999"}
print("welcome to SBI ATM")
print("please insert your card")
SBI_user_pin =input("pleace enter your 4 digit ATM PIN: ")
if len(SBI_user_pin) ==4:
    if SBI_user_pin in SBI_VAMSI_BUDUMURU_AC_DETAILS['ATM PIN']:
        print("the pin correct")
    else:
        print("you have entered invaild pin")
else:
    print("pls enter 4 digit pin")
'''

per_num = int(input("Enter a number: "))
fact_all = 0
for j in range(1,per_num):
    if per_num % j == 0:
        fact_all += j
if fact_all == per_num:
    print(f"{per_num} is the perfect num")
else:
    print(f"{per_num} is not a perfect num")



