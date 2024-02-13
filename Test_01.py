"""Test"""

import re
string = ''

# Task 0
"""
Найти в тексте
Input:  *
Output: *
"""
regex = r''
res = re.findall(regex, string)




# Task 0
"""

Input:  
Output: 
"""
import re

# s = input()
s = '[^START]Text балалайка гиппопотам{(END.)}'
regex = '(?<=\[\^START\]).*(?={\(END\.\)})'

res = re.findall(regex, s)
[print(_) for _ in res]

# res = re.finditer(regex, s)
# [print(_.group()) for _ in res]
