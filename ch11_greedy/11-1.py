# 모험가 길드
n = int(input())
adventurer = list(map(int, input().split()))
adventurer.sort()
count = 0
result = 0

for man in adventurer:
    count += 1

    if man == count:
        result += 1
        count = 0

print(result)