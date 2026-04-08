#recurcive function
#-------------------
'''recursion is a programing technique where a function calls it self
either directly or indirectly solve a problem by recursion is especially useful for problem
by breaking it into smaller, simpler subproblemrecursion is especially useful for problems that
can be divided into identical'''

'''
def correct_pin(self):
    while self.remaining_attempts > 0:
        user_pin = input("Enter 4 digit PIN: ")
        
        if len(user_pin) == 4 and user_pin == self.user_info["ATM PIN"]:
            print("✔️ Welcome to the ATM")
            return True
        else:
            self.remaining_attempts -= 1
            
            if self.remaining_attempts > 0:
                print(f"❌ Invalid PIN. Attempts left: {self.remaining_attempts}")
    else:
                print("⚠️ Card blocked. Please contact customer")
                return False

'''

any = "python is a language"
vowel_list =[]
con_list =[]
def vowel_con(any,vowel_list,con_list):
    for j in any:
        if j in "AEIOUaeiou":
            vowel_list.append(j)
        else:
            con_list.append(j)
    print(f"{vowel_list} these are all vowel in the string")
vowel_con(any,vowel_list,con_list)    







































