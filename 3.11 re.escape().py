#  3.11 re.escape()
""""""

"""
re.escape(pattern) - экранирует специальные символы в pattern. 
Полезно, если нужно использовать полученную строку как регулярное выражение, 
но в ней могут содержаться спецсимволы.

Если в метод передавать не сырую строку, 
а обычную - некоторые символы могут экранироваться и "потеряться". 
В итоге вы получите немного не ту строку для регулярного выражения, которую вы ожидали.
"""
# Примеры использования:
import re

print(re.escape(r'https://stepik.org/lesson/694442/step/1?unit=694231'))
# Выводит https\:\/\/stepik\.org\/lesson\/694442\/step\/1\?unit\=694231


# *******************************************************************


# Task 01
import re
print(re.escape(r'<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[]^_`abcdefghijklmnopqrstuvwxyz{|}~абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ !"#$%&\'()*+,-./0123456789:;'))


# Task 02
"""
Input:  https://www.youtube.com/watch?v=dQw4w9WgXcQ
Output: https://www\.youtube\.com/watch\?v=dQw4w9WgXcQ
"""
import re

s = input()
print(re.escape(rf'{s}'))

# без стандартного импорта
print(__import__('re').escape(input()))
