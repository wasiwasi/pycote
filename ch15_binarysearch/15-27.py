# 정렬된 배열에서 특정 수의 개수 구하기
from bisect import bisect_left, bisect_right

N, x = map(int, input().split())
progression = list(map(int, input().split()))

if x not in progression:
    print(-1)
else:
    print(bisect_right(progression, x) - bisect_left(progression, x))
