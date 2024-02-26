# 3.10 re.subn()
""""""
"""
re.subn(pattern, replace, string, count=0, flags=0) 
выполняет ту же операцию, что и функция re.sub(), но возвращает кортеж.

Параметры:
- pattern - регулярное выражение
- replace - то, на что нужно заменить найденное вхождение
- string - строка, к которой нужно применить регулярное выражение
- count - необязательный аргумент, максимальное число вхождений, подлежащих замене. 
    Если этот параметр опущен или равен нулю, то произойдет замена всех вхождений.
- flags - флаги

Возвращаемое значение:
Кортеж (new_string, number_of_subs), где

new_string - новая строка, или старая, если не было совершено замен.
number_of_subs - количество сделанных замен
"""
# Примеры использования:
import re

pattern = r'[a-z]{3}'
replace = '111'
string = 'abc 123 def 456 fed 321 cba'

result = re.subn(pattern, replace, string)

print(result)  # ('111 123 111 456 111 321 111', 4)


# *******************************************************************


# Task 01
"""
Input:  Нужно удалить все знаки препинания в тексте: .?!,:
Output: Количество совершённых замен
"""
import re

pattern = r'[\.?!,:]'
replace = ''
string = input()
res = re.subn(pattern, replace, string)
print(res[1])


# Task 02
"""
Замените все цифры на X. 
Выведите полученную строку и количество совершённых замен.
Input:  65,905 views  Nov 19, 2022 
Output: ('XX,XXX views  Nov XX, XXXX ', 11)
"""
import re

pattern = r'\d'
replace = 'X'
string = input()
res = re.subn(pattern, replace, string)
print(res)
