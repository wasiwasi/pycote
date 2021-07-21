# 떡볶이 떡 만들기
import sys

n, m = map(int, sys.stdin.readline().rstrip().split())
array = list(map(int, sys.stdin.readline().rstrip().split()))

array.sort()
start = 0
end = max(array)
result = 0

while (start <= end):
    mid = (start + end) // 2
    total = 0
    for parts in array:
        if parts > mid:
            total += parts - mid
    if total < m:
        end = mid - 1
    else:
        result = mid
        start = mid + 1

print(result)
