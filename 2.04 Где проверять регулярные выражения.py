# 2.04 Где проверять регулярные выражения
""""""

# Для проверки регулярных выражений существуют специальные онлайн-сервисы. Из самых удобных выделю следующие:
"""
regex101
https://regex101.com/

pythex
https://pythex.org/
"""

# Для проверки сравнений двух текстов так же существуют специальные онлайн-сервисы.
"""
textcompare.ru/app
https://textcompare.ru/app

text.num2word.ru/
http://text.num2word.ru/

prostudio.ru/tools/compare-text/
https://prostudio.ru/tools/compare-text/
"""



"""
английский/русский алфавит, цифры, или символы:
<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[]^_`abcdefghijklmnopqrstuvwxyz{|}~абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ !"#$%&\'()*+,-./0123456789:;
"""

# Похожая строчка
from string import printable

print(printable)
# 0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
#
# 

# "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~
#
# \x0b\x0c"
