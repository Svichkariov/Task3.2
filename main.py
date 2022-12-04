"""
2. Базовые операции со строками.
Найти самое длинное слово в введенном предложении
"""

s1 = input().split()
symbol = -1
big_word = ""

for i in s1:
    if symbol < len(s1):
        symbol += 1
    if len(i) > len(big_word):
        big_word = i
print(big_word)