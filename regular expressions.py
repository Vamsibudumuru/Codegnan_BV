'''REGULAR EXPRESSIONS(REGEX)
--------------------------
--->THIS REGULAR EXPRESSION OR REGEX IS A SEQUENNCE OF CHARACTERS THAT FORMS A SEARCHING PATTERN.
--->TO USE THIS WE HAVE TO IMPORT RE, WHICH WILL UNLOCK THE PACKAGE

FUNCTIONS
---------
1.FINDALL['a','a','a']
--->BY USING THIS FUNCTION,IT WILL FIND ALL SEQUENCE IN THE STRING
SYNTAX:--> re.findall(:metachar",variable_name)
import re
any = "python is a language"
so = re.findall("a",any)
print(so)


2.SEARCH
--------
--->BY USING THIS FUNCTION, IT WILL ONLY FIND FIRST SEQUENCE IN THE STRING
SYNTAX:--> re.search("metachar",variable_name)


import re
any = "python is a language"
so = re.search("a",any)
print(so)


METACHARACTERS
--------------
--->METACHARACTERS ARE USED TO FORM SEARCHING PATTERN
1.[]
----
--->IN THIS META CHARACTER WE CAN SEARCH FOR [A-Z],[A-Z],[0-9]

import re
any = "this method can read the entire file and return into list"
so = re.findall("[a-z]",any)
print(so)



some = "by using this function, it will only find first sequence in the"
an = re.search("[a]",some)
print(an)


2.dot(.)
--->THIS META CHRACTER WILL FORM A SEARCHING PATTERN AS IT WILL TAKE ANY SINGLE CHARACTER FOR (.)

import re
we = "hello"
the = re.findall("h...o",we)
thing = re.search("he..o",we)
print(the)
print(thing)


3.^
---
--->THIS IS USED TO FIND THE STRING IS STARTING WITH THE SEQUENCE OR NOT
SYNTAX:--->re.findall("metacharacter",variable_name)

import re
how = "THIS IS USED TO FIND THE STRING IS STARTING WITH THE SEQUENCE OR NOT"
who = re.findall("^this is", how)
then = re.search("^this is",then)
print(who)
print(then)


4.$
---
--->THIS IS USED TO FIND THE STRING IS ENDING WITH THE SEQUENCE OR NOT
SYNTAX:--> re.findall("$",variable_name)

import re
out = "THIS IS USED TO FIND THE STRING IS ENDING WITH THE SEQUENCE OR NOT"
one = re.findall("sequence $" ,out)
two = re.search("this$", out)
print(one)
print(two)


5.*
---
--->THIS META CHARACTER WILL FORM A SEARCHING PATTERN AS IT WILL TAKE ANY ZERO OR MORE CHARACTER FOR (*)
SYNTAX:--> findall(".*",variable_name)
import re
kanna = "THIS META CHARACTER WILL FORM A SEARCHING PATTERN AS IT WILL"
gk = re.findall("c.*i",kanna)
nk = re.search("t.*",kanna)
print(gk)
print(nk)



6.+
---
--->THIS META CHARACTER WILL FORM A SEARCHING PATTERN AS IT WILL TAKE ANY one OR MORE CHARACTER FOR (+)
SYNTAX --> re.search(".+",variable_name)

import re
kanna = "THIS META CHARACTER WILL FORM A SEARCHING PATTERN AS IT WILL"
gk = re.findall("an.+y",kanna)
msd = re.search("t.+",kanna)
print(gk)
print(msd)


7.?
---
--->THIS META CHARACTER WILL FORM A SEARCHING PATTERN AS IT WILL TAKE ANY ZERO OR ONE CHARACTER FOR(?)
SYNTAX:---> re.findall(".?",Variable_name)
'''
import re
any = "this meta character"
an = re.findall("Th.{5}",any)
print(an)


-----------------------------------------------------------------------------
'''


8.{}
----------
---> This meta character will form asearching pattern as we can mention the size in the {}
syntax --> re.search(".{size},variable")

9.
----
--> this meta character will form a searching pattern as it consider right or left any string is present or not for (  )

speical sequence:
--------------------
a special sequence is a \ followed by one of the characters in the list below, and has a

special meaning:
\A
----
return a match if the specified characters are at the beginning of thr string
eg: "\Athe"

'''
import re
any = "This meta character"
an = re.findall("Th..?",any)
print(an)

import re
can = "This meta character will form asearching pattern as we can mention the size in the {}"
a = re.findall(".{25}",can)
print(a)

import re
txt = "The rain in spain"
x = re.findall



speical sequence:
--------------------
a special sequence is a \ followed by one of the characters in the list below, and has a

special meaning:
\A
----
return a match if the specified characters are at the beginning of thr string
eg: "\Athe"

\b - returns a match where the specified characters are at the beginning or at the end of a word
eg: r"\bain"


\s - return a match where the string contains a white space
character
eg: "\s"
'''
















