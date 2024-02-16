# 3.4 Match - re.match()
""""""
"""
re.match(pattern, string, flags=0)
то же самое, что и re.search(), но ищет совпадение в начале строки.

Параметры:
pattern - регулярное выражение
string - строка, к которой нужно применить регулярное выражение
flags - флаги

Возвращаемое значение:
Объект Match, если совпадение было найдено
None, если нету совпадений
"""


# Task 01
"""
Найти первое слово в начале строки.
- Состоит как минимум из одной буквы
- Используются буквы латинского  алфавита обоих регистров
Input:  На вход программе подаётся 1 строка.
Output: 
"""
import re
pattern = r'(?i)[a-z]+'
string = input()
res = re.match(pattern, string)
if res:
    print(f"Первое слово в предложении: {res.group(0)}")


# Task 02
"""
- Seed-фраза - это последовательность из 12, 18 или 24 случайных слов
- В данном случае нужно проверять, что текст начинается как минимум с 12 слов
- Слова состоят из букв латинского алфавита нижнего регистра
- Между словами могут стоять только пробелы
Input:  oil one fix edit two maid boil see link old red ten
Output: возможно, это seed-фраза
"""
import re

string = input()
for el in [12, 18, 24]:
    pattern = rf'(?:[a-z]+\s?){{{el}}}'
    res = re.match(pattern, string)
    if res and len(res.group().split()) == el:
        print('возможно, это seed-фраза')
        break
# else:
#     print('не seed-строка')


# Task 03
"""
Из строки с адресом электронной почты, вывести всё содержимое, до символа @
Input:  example@gmail.com
Output: example
"""
import re
pattern = r'\w+(?=@)'
string = input()
res = re.match(pattern, string)
if res:
    print(res.group())


# Используя группы можно обойтись без lookahead
import re
pattern = r"(.+)@"
string = input()
res = re.match(pattern, string)
if res:
    print(res[1])
