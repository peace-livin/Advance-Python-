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

'''
[a-z] a to z
[abc] a or b or c
[A-Z] A to Z
[0-9] 0 to 9
[a-zA-Z0-9] a to z or A to Z or 0 to 9
[^a-zA-Z0-9] not a to z or A to Z or 0 to 9


pre defined character class
\d digit
\D not digit
\w word character
\W not word character
\s whitespace
\S not whitespace
\b word boundary    
\B not word boundary
'''


matcher=re.finditer("\w","abc$56CDF7d&^%$#@#$")

for match in matcher:
    print(match.start(),'-------',match.end(),'------',match.group())