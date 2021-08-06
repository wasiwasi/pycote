# 안테나
n = int(input())
houses = list(map(int,input().split()))
houses.sort()
# 중앙에서 가장 가까운 집을 찾음
print(houses[(n - 1) // 2])
     