# 3.7 re.findall()
""""""

"""
re.findall(pattern, string, flags=0) - возвращает список всех найденных совпадений.

Параметры:
pattern - регулярное выражение
string - строка, к которой нужно применить регулярное выражение
flags - флаги

Возвращаемое значение:
Список совпадений, если они есть
Пустой список, если совпадений нет


Примеры использования:
import re

pattern = r'\d{3}'
string = 'abc 123 def 456 fed 321 cba'

result = re.findall(pattern, string)

print(result) # ['123', '456', '321']
"""


# Task 01
"""
Нужно найти последовательности, подходящие по следующим условиям:
- Начинается с https://imgur.com/
- Потом идёт 7 символов из следующего диапазона: a-z, A-Z, 0-9
"""
import re

pattern = r'https://imgur\.com/[a-zA-z0-9]{7}'
string = input()
res = re.findall(pattern, string)
for el in res:
    print(el)


# Task 02
"""
Нужно найти последовательности, подходящие по следующим условиям:
- Начинается как минимум с одного из следующих символов: a-z, A-Z, 0-9, -, _
- Потом идёт @
- После @ снова идёт как минимум один из следующих символов: a-z, A-Z, 0-9
- Потом идёт .
- После . снова идёт как минимум один из следующих символов: a-z, A-Z
- Адрес почты не может быть подпоследовательностью.
"""
import re

pattern = r'(?i)(?!=\S)[a-zA-z0-9_-]+@[a-zA-z0-9]+\.[a-zA-z]+(?!\S)'
string = input()
res = re.findall(pattern, string)
for el in res:
    print(el)


# Task 03
"""
Найдите все даты в тексте. 
Датой в этом задании будем считать любую последовательность:
- nn/nn/nnnn
- nnnn/nn/nn
- nn.nn.nnnn
- nnnn.nn.nn
где n - любая цифра от 0 до 9.
"""
import re

pattern = r'\d{2}/\d{2}/\d{4}|\d{4}/\d{2}/\d{2}|\d{2}\.\d{2}\.\d{4}|\d{4}\.\d{2}\.\d{2}'
string = input()
res = re.findall(pattern, string)
for el in res:
    print(el)

pattern = r'(\d{2}/\d{2}/\d{4})|(\d{4}/\d{2}/\d{2})|(\d{2}\.\d{2}\.\d{4})|(\d{4}\.\d{2}\.\d{2})'
string = input()
res = re.findall(pattern, string)
for el in res:
    for i in el:
        if i:
            print(i)

pattern = r'(\d{2}/\d{2}/\d{4})|(\d{4}/\d{2}/\d{2})|(\d{2}\.\d{2}\.\d{4})|(\d{4}\.\d{2}\.\d{2})'
string = input()
res = re.finditer(pattern, string)
for el in res:
    print(el[0])  # print(el.group())


# Task 04
"""
- Нужно найти последовательности, подходящие по следующим условиям:
- Часы от 0 до 23
- Потом идёт :
- Минуты от 0 до 59
- Если в последовательности количество часов или минут меньше 10, то перед ним стоит 0
- Не является подпоследовательностью
"""
import re

pattern = r'\b(?:[01][0-9]|2[0-3]):[0-5][0-9]\b'
string = input()
res = re.findall(pattern, string)
for el in res:
    print(el)


# Task 05
"""
Выведите все ссылки, которые находятся в тегах <a...</a>:
<a target="_blank" href="https://stepik.org/">Hyperlink</a>
Должно вывести:
https://stepik.org/

Нужно найти последовательности, подходящие по следующим условиям:
- Ссылка находится в теге a
- Слева и справа от ссылки стоят двойные или одинарные кавычки
- Перед левой кавычкой стоит href=
- Сама ссылка может состоять из любых символов
- Длина ссылки как минимум 1 символ
"""
import re

pattern_a = r'<a .*?</a>'
pattern = r"(?:(?<=href=\")|(?<=href=\')).+?(?=\"|')"
string = input()
res = re.findall(pattern_a, string)
for el in res:
    print(re.search(pattern, el)[0])
