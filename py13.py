'''
# Take input from user "String Methods"
#Work on strings (text)
#Immutable ---> cannot change original string

text = input("Enter a string: ")

# ----------- Basic string transformations -----------
print("Original:", text)                   # prints original string
print("Lowercase:", text.lower())         # converts all letters to lowercase
print("Uppercase:", text.upper())         # converts all letters to uppercase
print("Title Case:", text.title())        # first letter of each word capital
print("Capitalized:", text.capitalize())  # only first letter capital

# ----------- Checking / validation methods -----------
print("Is alphabet:", text.isalpha())     # True if only letters (no spaces/numbers)
print("Is digit:", text.isdigit())        # True if only numbers
print("Is alphanumeric:", text.isalnum()) # True if letters + numbers (no spaces)
print("Starts with 'a':", text.startswith('a'))  # checks starting letter
print("Ends with 'z':", text.endswith('z'))      # checks ending letter

# ----------- Searching & replacing -----------
print("Count of 'a':", text.count('a'))   # counts how many times 'a' appears
print("Index of 'a':", text.find('a'))    # gives position of 'a' (-1 if not found)
print("Replace 'a' with '@':", text.replace('a', '@'))  # replaces characters

# ----------- Removing spaces -----------
print("Strip:", text.strip())             # removes spaces from both sides
print("Left strip:", text.lstrip())       # removes spaces from left side
print("Right strip:", text.rstrip())     # removes spaces from right side

# ----------- Splitting & joining -----------
words = text.split()                     # splits string into list of words
print("Split:", words)

joined = "-".join(words)                 # joins words with '-'
print("Joined:", joined)

# ----------- Length -----------
print("Length:", len(text))    # total number of characters
'''


#list methods
#A list in Python is a collection of items stored in a single variable.

#Items are separated by commas
#Written inside square brackets [ ]
#Can store different data types (int, string, float, etc.)
#Mutable → can be changed after creation

# Create a list
nums = [10, 20, 30]

print("Original list:", nums)

# ----------- Adding elements -----------
nums.append(40)        # adds element at end
print("Append:", nums)

nums.insert(1, 15)     # inserts 15 at index 1
print("Insert:", nums)

nums.extend([50, 60])  # adds multiple elements
print("Extend:", nums)

# ----------- Removing elements -----------
nums.remove(20)        # removes specific value
print("Remove:", nums)

nums.pop()             # removes last element
print("Pop last:", nums)

nums.pop(1)            # removes element at index 1
print("Pop index 1:", nums)

# ----------- Searching -----------
print("Index of 30:", nums.index(30))  # finds index of element
print("Count of 10:", nums.count(10))  # counts occurrences

# ----------- Sorting & reversing -----------
nums.sort()            # sorts list in ascending order
print("Sorted:", nums)

nums.reverse()         # reverses list
print("Reversed:", nums)

# ----------- Copying -----------
new_list = nums.copy() # creates a copy of list
print("Copied list:", new_list)

# ----------- Clearing -----------
nums.clear()           # removes all elements
print("Cleared list:", nums)
