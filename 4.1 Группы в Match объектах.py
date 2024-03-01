#  4.1 Группы в Match объектах
""""""

"""
Объект Match

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
"""


# *******************************************************************


# Task 01
"""
Нужно найти теги, подходящие по следующим условиям:
В начале тега стоит:
<p
Тут может быть последовательность символов минимально возможной длины
>
Внутри тега последовательность из любых символов минимально возможной длины
В конце тега стоит </p>
Input:  <p>Это параграф</p>
Output: Это параграф
"""
import re

regex = r'(<p.*?>)(?P<root>.*?(?=</p))'
string = input()

res = re.finditer(regex, string)
for el in res:
    if el.group('root'):
        print(el.group('root'))


# Task 02
"""
Напишите программу, которая будет находить ссылки и разделять их на части: протокол, адрес, параметры, якорь. 
Протокол и адрес у ссылок есть всегда.

Нужно найти ссылки, подходящие по следующим условиям:
Протокол https или http
После протокола идёт ://
Домен состоит из символов a-z, .
Путь состоит из символов a-z, 0-9, -, _, /
Параметры начинаются с ? и состоят из a-z, =, &, 0-9
Якорь начинается с # и состоит из a-z
Протокол и адрес у ссылок есть всегда, остальных частей может не быть
Ссылка не может быть подпоследовательностью

Input:  
В этом https://stepik.org/lesson/704265/step/2?unit=704697#test тексте https://example.com/ очень много 
https://keep.google.com/#home разных http://oldastoundingrelaxedlaugh.neverssl.com/online ссылок. 

Output: 
Полная ссылка: https://stepik.org/lesson/704265/step/2?unit=704697#test
Протокол: https | Домен: stepik.org | Параметры: ?unit=704697 | Якорь: #test

Полная ссылка: https://example.com/
Протокол: https | Домен: example.com | Параметры: None | Якорь: None

Полная ссылка: https://keep.google.com/#home
Протокол: https | Домен: keep.google.com | Параметры: None | Якорь: #home

Полная ссылка: http://oldastoundingrelaxedlaugh.neverssl.com/online
Протокол: http | Домен: oldastoundingrelaxedlaugh.neverssl.com | Параметры: None | Якорь: None
"""
import re

regex = r'(?P<protocol>https?)://(?P<domain>[a-z\.]+)[a-z0-9_/-]+(?P<argument>\?[a-z0-9=&]+)?(?P<anchor>#[a-z]+)?'
string = input()

res = re.finditer(regex, string)

for el in res:
    print(f'Полная ссылка: {el[0]}')
    print(
        f'Протокол: {el.group("protocol")} | Домен: {el.group("domain")} | '
        f'Параметры: {el.group("argument")} | Якорь: {el.group("anchor")}\n')
