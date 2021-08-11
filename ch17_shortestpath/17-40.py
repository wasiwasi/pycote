# 숨바꼭질
import heapq
INF = int(1e9)
n, m = map(int, input().split())
barn = [[] for _ in range(n + 1)]
distance = [INF] * (n + 1)

for _ in range(0, m):
    i, j = map(int, input().split())
    barn[i].append((j, 1))
    barn[j].append((i, 1))

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

q = []
distance[1] = 0
heapq.heappush(q, (distance[1], 1))
while q:
    dist, now = heapq.heappop(q)
    if dist > distance[now]:
        continue
    for i in barn[now]:
        cost = dist + i[1]
        if cost < distance[i[0]]:
            distance[i[0]] = cost
            heapq.heappush(q, (cost, i[0]))
number = 0
max_value = 0
count = 1

for i in range(1, n + 1):
    if distance[i] > max_value:
        number = i
        max_value = distance[i]
        count = 1
    elif distance[i] == max_value:
        count += 1
print(number, max_value, count)