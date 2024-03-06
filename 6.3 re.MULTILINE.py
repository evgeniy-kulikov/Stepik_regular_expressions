# 6.3 re.MULTILINE
""""""

"""
re.MULTILINE

При использовании флага спецсимволы ^ и $ будут совпадать не с началом и концом всего текста, 
а с началом и концом строк.

Полная версия:
re.MULTILINE

Сокращённая версия:
re.M

Встроенный флаг:
(?m)

Числовое представление:
8
"""
import re

string = '''
I like flags
I like flags
I like flags
'''

test1 = re.findall(r'^I like flags$', string, flags=re.MULTILINE)
test2 = re.findall(r'^I like flags$', string, flags=re.M)
test3 = re.findall(r'(?m)^I like flags$', string)

print(test1)  # ['I like flags', 'I like flags', 'I like flags']
print(test1 == test2 and test2 == test3)  # True


#  * * * * * * * * * *   T a s k   * * * * * * * * * *

# Task 01
"""

Input:  
Output: 
"""
import re, sys

text = ''.join(sys.stdin.readlines())
regex = r'(?m)^[$^]+$'
res = re.findall(regex, text)
print(res)


text = ''.join(sys.stdin.readlines())
regex = r'^[$^]+$'
res = re.findall(regex, text, flags=re.MULTILINE)
print(res)


# import re
#
# string = """
# $$^^$^$$4^^$^^$$$
# ^$^$
# ^$$^$^^^$^^$$^$$$$
# ^^^^$$S^$^$^$^$^^$$
# """
#
# regex = r'(?m)^[$^]+$'
# res = re.findall(regex, string)
# print(res)
