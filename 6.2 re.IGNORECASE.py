# 6.2 re.IGNORECASE
""""""

"""
e.IGNORECASE

При использовании флага регулярные выражения будут игнорировать регистр.

Полная версия:
re.IGNORECASE

Сокращённая версия:
re.I

Встроенный флаг:
(?i)

Числовое представление:
2
"""

import re

string = 'I like flags I LIKE FLAGS i like flags'

test1 = re.findall(r'I like flags', string, flags=re.IGNORECASE)
test2 = re.findall(r'I like flags', string, flags=re.I)
test3 = re.findall(r'(?i)I like flags', string)

print(test1)  # ['I like flags', 'I LIKE FLAGS', 'i like flags']
print(test1 == test2 and test2 == test3)  # True


#  * * * * * * * * * *   T a s k   * * * * * * * * * *


# Task 01
"""
Нужно исправить код, чтобы он смог заменить O на X, o на x
Новая буква должна быть такого же регистра, как и оригинальная.
Input:  LOST CXNTURY - CYBERSITY | scarlord - FALSE HOPE
Output: LXST CXNTURY - CYBERSITY | scarlxrd - FALSE HXPE
"""
import re

def get_x(match_obj):
    dictionary = {'o': 'x', 'O': 'X'}
    return dictionary[match_obj.group()]
    # return dictionary[match_obj.[0]]


string = input()
regex = r'(?i)o'

res = re.sub(regex, get_x, string)
print(res)


# Task 02
"""
Нужно исправить код, чтобы он смог заменить O на X, o на x
Новая буква должна быть такого же регистра, как и оригинальная.
Input:  LOST CXNTURY - CYBERSITY | scarlord - FALSE HOPE
Output: LXST CXNTURY - CYBERSITY | scarlxrd - FALSE HXPE
"""
import re

# string = input()

regex = r'(?i)привет'
res = re.findall(regex, string)
print(res)

# regex = r'привет'
# res = re.findall(regex, string, flags=re.I)
# print(res)
