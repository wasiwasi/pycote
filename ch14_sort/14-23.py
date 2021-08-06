# 국영수
n = int(input())
students = []
for _ in range(n):
    data = list(input().split())
    for i, score in enumerate(data[1:]):
        data[i + 1] = int(score)
    students.append(data)

students.sort(key = lambda x : (-x[1], x[2], -x[3], x[0]))

for student in students:
    print(student[0])