# 3.3 Match - re.search()
""""""

"""
re.search(pattern, string, flags=0) -  ищет первое совпадение в строке

Параметры:
pattern - регулярное выражение
string - строка, к которой нужно применить регулярное выражение
flags - флаги
Возвращаемое значение:
Объект Match, если совпадение было найдено
None, если нету совпадений

Пример:

pattern = r'\d{3}'
string = 'abc 123 def 456 fed 321 cba'
# Ищет только одно вхождение, самое первое
result = re.search(pattern, string)

print(result) # <re.Match object; span=(4, 7), match='123'>
"""


# Task 01
"""
найти первый хештег в тексте:
Начинается с символа #
После # стоит последовательность из латинских букв нижнего регистра
Выведите в консоль первый найденный хештег. 
Если его нет - ничего выводить не нужно.
Input:  Some #hashtags for you
Output: #hashtags
"""

import re

pattern = r'#[a-z]+'
string = input()
result = re.search(pattern, string)
if result is not None:
    print(result[0])


# Task 02
"""
Полёт на Марс
https://stepik.org/lesson/629511/step/3?unit=625388
На вход программе подаются 4 строки.
Найти строку, в которой есть последовательности код или Код. 
Получить номер этой строки и номер начала вхождения последовательности.
Иначе выведите строку: код не найден
"""
# string = ['Хочу полететь на Марс(',
#           'Секретный код: Dogecoin',
#           'Батут работает!',
#           'Где ключи от моей Tesla?']
import re

pattern = r'\b[кК]од\b'
string = [input() for el in range(4)]
line = 0
flag = True
for el in string:
    line += 1
    res = re.search(pattern, el)
    if res:
        print(line, res.start())
        flag = False
        break
if flag:
    print('код не найден')

# решение на любое количество строк
import re, sys

line = 0
pattern = r'\b[кК]од\b'
for el in sys.stdin:
    line += 1
    res = re.search(pattern, el)
    if res:
        print(line, res.start(0))
        break
else:
    print('код не найден')


# Task 03
"""
Нужно найти первый попавшийся ключ. Нужные ключи в виде:
Activation key: XXXXX-XXXXX-XXXXX-XXXXX-XXXXX
X - любая цифра или латинская буква в верхнем регистре
Перед нужным ключом должна стоять строка Activation key:
На вход программе подаётся 5 строк. 
Гарантируется, что в этих строках есть как минимум 1 ключ.
Выведите в консоль ключ, который был найден. 
"""
import re

pattern = r'(?<=Activation key:\s)(?:([A-Z0-9]{5}-){4}[A-Z0-9]{5})(?!\S)'
string = [input() for el in range(5)]

for el in string:
    res = re.search(pattern, el)
    if res:
        print(res[0])
        break


# решение на любое количество строк
import re

res = False
pattern = r'(?<=Activation key:\s)(?:([A-Z0-9]{5}-){4}[A-Z0-9]{5})(?!\S)'

while not res:
    res = re.search(pattern, input())
print(res.group())


# Task 04
"""
Нужно найти ключ t и его значение:
Значением является последовательностью из арабских цифр, символов . и +
Перед значением стоит t=
На вход подаётся 1 строка с данными
Вывести ключ t и его значение.
"""
import re

pattern = r't=[0-9\.\+]+'
res = re.search(pattern, input())
print(res.group())
