# 왕실의 나이트

data = input()

process_dict = { "a" : 1, "b" : 2,  "d" : 4,  "e" : 5,  "f" : 6,  "g" : 7,  "h" : 8 }
column = process_dict[data[0]]  # int형으로 바꿈 ex)a1 == 11
row = int(data[1])
result = 8  # 못가는 곳을 빼기연산하기 위해 최대경로 8로 초기화

steps = [(-2, 1), (-2, -1),(2, 1), (2, -1), (1, 2) , (-1, 2), (1, -2), (-1, -2)]

for step in steps:
    nx = row
    ny = column

    nx += step[0]
    ny += step[1]

    if (nx < 1 | nx > 8):
        result -= 1
    elif (ny < 1 | nx > 8):
        result -= 1

print(result)