# 4.5 Функции в re.sub() и re.subn()
""""""

"""
Вместо строки, на которую нужно заменить вхождение, в re.sub() и re.subn() 
можно передать функцию, которая будет генерировать ту самую строку.
В функцию передаётся Match объект, и теперь мы можем получать доступ к группам, 
а также как-либо изменять и обрабатывать эти данные.
"""
import re

def func(match_obj):
    el = str(len(match_obj[0]))
    return el

regex = r'[a-zA-Z]{1,}'
text = 'Lorem#dummy-text_of*the=printing>and^typesetting<industry.'

res_func = re.sub(regex, func, text)

# lambda mur: str(len(mur[0]))  равнозначна func(match_obj)
res_lambda = re.sub(regex, lambda str_obj: str(len(str_obj[0])), text)

print(res_func)  # 5#5-4_2*3=8>3^11<8.
print(res_func == res_lambda)  # True
print(res_lambda)  # 5#5-4_2*3=8>3^11<8.


#  * * * * * * * * * *   T a s k   * * * * * * * * * *


# Task 01
"""
Найдите все числа в тексте и возведите их в квадрат.
Input:  2 в квадрате это 4
Output: 4 в квадрате это 16
"""
import re

string = input()
regex = r'\d+'

def square(inst):
    return str(int(inst[0]) ** 2)

res = re.sub(regex, square, string)
print(res)

# res = re.sub(regex, lambda inst: str(int(inst[0]) ** 2), string)
# print(res)


# Task 02
"""
Нужно найти все слова, которые начинаются на букву А или а 
и заменить их на удалено(n), где n - длина удалённого слова.
Input:  А роза упала на лапу Азора.
Output: удалено(1) роза упала на лапу удалено(5).
"""
import re

string = input()
regex = r'\b[Аа]\w*'

res = re.sub(regex, lambda el: f'удалено({len(el[0])})', string)
print(res)


# Task 03
"""
В строке am заменить на pm, 
и pm заменить на am.
Input:  It's already 12:00am and pm am.
Output: It's already 12:00pm and am pm.
"""
import re

string = input()
regex = r'[ap]m'

res = re.sub(regex, lambda el: "pm" if el[0] == "am" else "am", string)
# res = re.sub(regex, lambda el: f'{"pm" if el[0] == "am" else "am"}', string)

print(res)


# Task 04
"""
Найти все числа в тексте, и проверить, кратно число 3 или нет:
- Если кратно, то заменить его на это же число, разделённое на 3
- Если нет - оставить его как есть
Input:  500 501 502 503 504
Output: 500 167 502 503 168
"""
import re

string = input()
regex = r'\d+'

res = re.sub(regex, lambda el: f'{int(el[0]) // 3 if not int(el[0]) % 3 else el[0]}', string)
print(res)


# Вариант
def func(match_obj):
    el = int(match_obj.group())
    return str(el // 3) if not el % 3 else str(el)

regex = r'\d+'
print(re.sub(regex, func, string))
