#  5.1 Pattern | re.compile()
""""""

"""
re.compile(pattern, flags=0) - метод, который позволяет вручную компилировать регулярные выражения.

Параметры:
pattern - регулярное выражение
flags - флаги
Возвращаемое значение:
Объект Pattern - скомпилированное регулярное выражение

При использовании функции re.compile создается объект RegexObject, 
у которого есть несколько дополнительных возможностей, которых нет в объекте MatchObject

У объекта который возвращает re.compile, доступны методы search, match, finditer, findall. 
Это те же функции, которые доступны в модуле глобально, но теперь их надо применять к объекту.

https://pyneng.readthedocs.io/ru/latest/book/15_module_re/compile.html#re-compile
"""
import re

regex = re.compile(r'[a-zA-Z]{1,}')  # Регулярное выражение скомпилировано
print(regex)  # re.compile('[a-zA-Z]{1,}')

# Теперь можно использовать методы:
print(regex.findall('Some words.'))  # ['Some', 'words']
print(regex.sub('deleted', 'Some words again.'))  # deleted deleted deleted.

"""
После компиляции регулярного выражения, функция re.compile() возвращает объект Pattern.
Именно через этот объект можно обратиться ко всем функция из модуля re, 
но они будут уже не функциями, а методами этого объекта.

import re

pattern = re.compile(r'(?P<group1>[a-zA-Z]{1,})')

Атрибуты

pattern.flags
Каждый флаг - хранится как какое-либо число. pattern.flags возвращает сумму этих чисел:
print(pattern.flags) # 32

pattern.groups
Возвращает количество групп в регулярном выражении:
print(pattern.groups) # 1

pattern.groupindex
Возвращает словарь, в котором ключи - именованные группы, а значения - номера этих групп:
print(pattern.groupindex) # {'group1': 1}

pattern.pattern
Возвращает регулярное выражение:
print(pattern.pattern) # (?P<group1>[a-zA-Z]{1,})
 

Методы
Благодаря объекту Pattern в методах search(), match(), fullmatch(), finditer(), findall() 
появляются дополнительные параметры:

pos - позволяет указывать индекс в строке, с которого надо начать искать совпадение

endpos - указывает, до какого индекса надо выполнять поиск
"""
import re

pattern = re.compile(r'(?P<group1>[a-zA-Z]{1,})')

match1 = pattern.match("Some words.", 4)  # None
match2 = pattern.match("Some words.", 5)  # <re.Match object; span=(5, 10), match='words'>


#  * * * * * * * * * *   T a s k   * * * * * * * * * *


# Task 01
"""
Скомпилировать регулярное выражение, которое находит все mac-адреса: 
nn:nn:nn:nn:nn:nn, где n это 16-ричное число от 0 до F, 
и записать его в переменную pattern.
"""
import re

regex = r'[0-9A-F]{2}(?::[0-9A-F]{2}){5}'
pattern = re.compile(regex)

# string = input()
# res = regex.findall(string)
# print(res)


# Task 02
"""
Найти первое слово, состоящее из a-z в определённом диапазоне. Слово не может являться подпоследовательностью.
На вход программе подаётся 3 строки:
* Текст
* Начальная позиция для поиска
* Конечная позиция для поиска
Если в полученном диапазоне есть слово, то нужно его вывести.
Input:  soda senior tuition library task tone few torch vacuum
        2
        29
Output: senior
"""
import re

regex = r'\b[a-z]+'
pattern = re.compile(regex)

string, pos, endpos = (input() for _ in range(3))

res = pattern.search(string, pos=int(pos), endpos=int(endpos))
if res:
    print(res[0])
