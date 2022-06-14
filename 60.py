from dataclasses import replace


s1 = str(input("請輸入一單字："))

if 'a'or'A' in s1:
    s1 = s1.replace('a','.')
    s1 = s1.replace('A','.')
if 'e'or'E' in s1: 
    s1 = s1.replace('E','.')
    s1 = s1.replace('e','.')
if 'i'or'I' in s1:
    s1 = s1.replace('I','.') 
    s1 = s1.replace('i','.')
if 'o'or'O' in s1: 
    s1 = s1.replace('O','.')
    s1 = s1.replace('o','.')
if 'u'or'U' in s1: 
    s1 = s1.replace('U','.')
    s1 = s1.replace('u','.')
print(s1)