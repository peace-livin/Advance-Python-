# regular expression is a sequence of characters that defines a search pattern

# compiler

import re

# target="abababaaba"
# pattern= re.compile("ab")


# matcher=re.finditer(pattern,target)

# for match in matcher:
#     print(match.start(),'-------',match.end(),'------',match.group())
    
    
# target="abababaaba"


# matcher=re.finditer("aba",target)

# for match in matcher:
#     print(match.start(),'-------',match.end(),'------',match.group())
    
# *****      character class **** 

# '''
# [a-z] a to z
# [abc] a or b or c
# [A-Z] A to Z
# [0-9] 0 to 9
# [a-zA-Z0-9] a to z or A to Z or 0 to 9
# [^a-zA-Z0-9] not a to z or A to Z or 0 to 9
# a+ atmost one a
# a* atleast one a
# a? atleast one a

# pre defined character class
# \d digit
# \D not digit
# \w word character
# \W not word character
# \s whitespace
# \S not whitespace
# \b word boundary    
# \B not word boundary
# '''


# matcher=re.finditer("a?","abc$56CDF7d&^%$#@#$")

# for match in matcher:
#     print(match.start(),'-------',match.end(),'------',match.group())                                                                                                                                                                                                                                                                                                                                                                                                              


# match function 
#  match function is used to find the first occurrence of a pattern in a string


import re
# pattern= input("Enter the pattern:")
# target="python is a good language"

# m=re.match(pattern,target)
# if m!=None:
#     print("Match found")
    
# else:
#     print("No match found")


# search function 
#search function is used to find all occurrences of a pattern in a string
# import re
# pattern= input("Enter the pattern:")
# target="python is a good language"

# m=re.search(pattern,target)
# if m!=None:
#     print("Match found")
    
# else:
#     print("No match found")


# fullmatch function 
#fullmatch function is used to find all occurrences of a pattern in a string
# import re
# pattern= input("Enter the pattern:")
# target="python is a good language"

# m=re.fullmatch(pattern,target)
# if m!=None:
#     print("Match found")
# else:
#     print("No match found")


#substitute function
# import re
# res=re.sub("a","&","aabbaaabbaba")
# print(res)


# res=re.subn("a","&","aabbaaabbaba")
# print(res)


# practice q1): create a pattern to find mobile number and digit is 10 

# import re
# pattern= "[6-9][0-9]{9}"
# mob=input("Enter the mobile number:")
# m=re.fullmatch(pattern,mob)
# if m!=None:
#     print("Valid mobile number")
# else:
#     print("Invalid mobile number")


# Q2).mahrashtra number plate pattern 

import re
pattern= "[M][H][0][0-5][A-Z][A-Z][0-9]{4}"
plate=input("Enter the plate number:")
m=re.fullmatch(pattern,plate)
if m!=None:
    print("Valid plate number")
else:
    print("Invalid plate number")