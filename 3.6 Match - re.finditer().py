# 3.6 Match - re.finditer()
""""""

"""
re.finditer(pattern, string, flags=0) 
- возвращает итератор Match объектов с вхождениями pattern в строке string.

Параметры:
pattern - регулярное выражение
string - строка, к которой нужно применить регулярное выражение
flags - флаги

Возвращаемое значение:
Итератор Match объектов

import re
pattern = r'\d{3}'
string = 'abc 123 def 456 fed 321 cba'
result = re.finditer(pattern, string, 0)

for i in result:
    print(i)

# В данном примере будет выведено:
# <re.Match object; span=(4, 7), match='123'>
# <re.Match object; span=(12, 15), match='456'>
# <re.Match object; span=(20, 23), match='321'>
"""


# Task 01
"""
Нужно найти последовательности, подходящие по следующим условиям:
Состоит из \w
Длина - максимально возможная
На вход программе подаётся 1 строка.
"""
import re

pattern = r'\w+'
string = input()
res = re.finditer(pattern, string)
for el in res:
    print(el.group())


# Task 02
"""
Нужно найти последовательности, подходящие по следующим условиям:
Состоит из букв латинского и кириллического алфавитов обоих регистров
Длина - 5 букв
Не является подпоследовательностью
"""
import re

pattern = r'(?i)\b[a-zа-яё]{5}\b'
string = input()
res = re.finditer(pattern, string)
for el in res:
    print(el.group())


# Task 03
"""
Получите все числовые значения, после которых идёт знак ₽. 
Значения с неразрывным пробелом &nbsp; игнорируем.
Нужно найти последовательности, подходящие по следующим условиям:
Состоит из цифр и ,
В конце последовательности стоит  ₽
"""
import re

pattern = r'\d+,?\d*\s₽'
string = input()
res = re.finditer(pattern, string)
for el in res:
    print(el.group())
