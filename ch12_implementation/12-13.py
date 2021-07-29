# 치킨배달
from itertools import combinations

n, m = map(int, input().split())
homes = []
chickens = []
for r in range(n):
    city = list(map(int, input().split()))
    for c in range(n):
        if city[c] == 1:
            homes.append((r, c))
        elif city[c] == 2:
            chickens.append((r, c))

situation = list(combinations(chickens, m))
result = 1e9

for remaining_store in situation:
    total = 0
    for home_x, home_y in homes:
        distance = 1e9
        for x, y in remaining_store:
            # 집에서 가장 가까운 치킨집 거리
            distance = min(distance, abs(home_x - x) + abs(home_y - y))
        # 한 상황에서의 치킨거리 총합
        total += distance
    result = min(result, total)
    
print(result)