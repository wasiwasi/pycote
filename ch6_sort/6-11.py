# 성적이 낮은 순서로 학생 출력하기

from abc import abstractproperty


n = int(input())
array = []

for _ in range(n):
    array.append(tuple(input().split()))

result = sorted(array, key = lambda score: score[1])

for student in result:
    print(student[0], end = ' ')
    