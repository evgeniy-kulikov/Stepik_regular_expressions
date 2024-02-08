"""

Input:  *
Output: *
"""

# Task 06
"""

Input:  
Output: 
"""
import re

# s = input()
s = 'Я бежал... Пока мышцы не стало жечь огнем, а кровь не стала едкая, как кислота... И тогда... Я побежал дальше...'
regex = r'\.{3}'

res = re.findall(regex, s)
print(res)