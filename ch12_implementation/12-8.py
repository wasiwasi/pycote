# 문자열 재정렬

from abc import abstractproperty


s = input()

character = []
number = 0 

for data in s:
    if data.isalpha():
        character.append(data)
    else:
        number += int(data)

character.sort()

for c in character:
    print(c, end = '')
print(number)
