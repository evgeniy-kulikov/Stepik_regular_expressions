#  6.9 re.NOFLAG
""""""

"""
re.NOFLAG 
Указывает, что в функции/методе не применяется флаг.

Полная версия:
re.NOFLAG

Сокращённая версия:
Нет

Встроенный флаг:
Нет

Числовое представление:
0
"""
import re
def myfunc(text, flags=re.NOFLAG):
    return re.match(text, flags)
