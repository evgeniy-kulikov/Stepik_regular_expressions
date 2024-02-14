# 3.2 Объект Match
""""""

"""
Методы и атрибуты объекта Match:
expand()
group()
groups()
groupdict()
start()
end()
span()
lastindex
lastgroup
pos
endpos
re
string


* * * * *   group([group1, ...])   * * * * * 
Возвращает найденное совпадение по номеру группы.
match.group()   # Если в метод не передать аргумент, то он по умолчанию выведет нулевую группу
match.group(0)  # Можно передать номер нужной группы в метод
match[0]        # Благодаря геттеру в Match-объекте к группам можно обращаться с помощью квадратных скобок


* * * * *   start(__group=0), end(__group=0)   * * * * * 
Методы start и end возвращают индексы начала и конца совпадения с регулярным выражением группы, 
номер которой был передан в метод:
match.start()   # по умолчанию выведет индексы для нулевой группы
match.end()
match.start(0)  # Можно передать номер нужной группы в метод
match.end(0)


* * * * *   re   * * * * * 
Если обратиться к атрибуту, то можно получить регулярное выражение, 
которое использовалось для поиска:
print(match.re) # re.compile('паттерн')


* * * * *   string   * * * * * 
Если обратиться к атрибуту, то можно получить строку, в которой искались совпадения:
print(match.string) # Строка для поиска


* * * * *   pos   * * * * * 
!!!  Используется вместе с объектом Pattern
pos - это позиция, с которой функция начинает искать совпадения (значение по умолчанию: 0).
print(match.pos) # 0


* * * * *   endpos   * * * * * 
!!!  Используется вместе с объектом Pattern
endpos - это позиция, до которой функция начинает искать совпадения 
(значение по умолчанию: индекс последнего символа в строке).
print(match.pos) # 46
"""


# Task 01
"""
https://stepik.org/lesson/703166/step/5?unit=703492
Получаем информацию
"""
import re
match = re.match(input(), input())
print(match.group(0))
print(match.start(0))
print(match.end(0))
print(match.pos)
print(match.endpos)
print(match.re)
print(match.string)

# попытка на оригинальность
match = re.match(input(), input())
attrs = ["group", "start", "end", "pos", "endpos", "re", "string"]
for idx, attr in enumerate(attrs):
    if idx < 3:
        print(getattr(match, attr)(0))
    else:
        print(getattr(match, attr))

# Task 02
"""
Найти в тексте
Input:  *
Output: *
"""
import re

match = re.match(input(), input())
if match is not None:
    print(match.group())
