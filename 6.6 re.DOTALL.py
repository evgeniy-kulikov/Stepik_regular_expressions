#  6.6 re.DOTALL
""""""

"""
re.DOTALL

Точка . теперь будет соответствовать любому символу. 
Если флаг не используется - точка соответствует любому символу, кроме символа новой строки.

Полная версия:
re.DOTALL

Сокращённая версия:
re.S

Встроенный флаг:
(?s)

Числовое представление:
16
"""

import re

string = '''
I like flags
I like flags
I like flags
'''

test1 = re.findall(r'I like flags.', string, flags=re.DOTALL)
test2 = re.findall(r'I like flags.', string, flags=re.S)
test3 = re.findall(r'(?s)I like flags.', string)

print(test1)  # ['I like flags\n', 'I like flags\n', 'I like flags\n']
print(test1 == test2 and test2 == test3)  # True


#  * * * * * * * * * *   T a s k   * * * * * * * * * *


# Task 01
"""
Дан большой текст, который состоит из нескольких строк, он находится в переменной text.
Найдите в нём текст от start до end
Input:  start
        Каждое
        Слово
        На
        Новой
        Строке
        end
Output: ['\nКаждое\nСлово\nНа\nНовой\nСтроке\n']
"""
import re, sys
text = ''.join(sys.stdin.readlines())

regex = r'(?s)(?<=start).*(?=end)'
res = re.findall(regex, text)
print(res)


# Вариант
regex = r'(?<=start).*(?=end)'
res = re.findall(regex, text, re.DOTALL)
# res = re.findall(regex, text, re.S)
# res = re.findall(regex, text, 16)
print(res)
