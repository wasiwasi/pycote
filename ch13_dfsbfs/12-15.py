# 특정 거리의 도시 찾기
from collections import deque

n, m, k, x = map(int, input().split())
roads = [[] for _ in range(n + 1)]
result = []
for _ in range(m):
    a, b = map(int, input().split())
    roads[a].append(b)

distance = [-1] * (n + 1)
distance[x] = 0

q = deque([x])
while q:
    now = q.popleft()
    for next_node in roads[now]:
        if distance[next_node] == -1:
            distance[next_node] = distance[now] + 1
            q.append(next_node)

if k not in distance:
    print(-1)   
else:
    for i in range(n + 1):
        if distance[i] == k:
            print(i)
