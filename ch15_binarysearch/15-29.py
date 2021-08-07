# 공유기 설치
n, c = map(int, input().split())
houses = []
for _ in range(n):
    houses.append(int(input()))
houses.sort()
# 최소거리, 최대거리
start = 1
end = houses[-1] - houses[0]
result = 1
while start <= end:
    count = 1
    # 공유기 사이의 거리
    mid = (start + end) // 2
    point = houses[0]
    for i in range(n):
        if houses[i] - point >= mid:
            point = houses[i]
            count += 1
    if count >= c:
        start = mid + 1
        result = mid
    elif count < c:
        end = mid - 1
print(result)