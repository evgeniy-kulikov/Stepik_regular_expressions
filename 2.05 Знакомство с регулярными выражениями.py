# 2.05 Знакомство с регулярными выражениями
""""""
str_ = 'Привет, как дела? Привет, ок'

str_pattern = r'Привет'

print(re.findall(str_pattern, str_ ))