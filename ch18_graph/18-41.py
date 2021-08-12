# 여행 계획
from collections import deque
n, m = map(int, input().split())
graph = [[] for _ in range(n)]
for i in range(n):
    data = list(map(int, input().split()))
    for j, d in enumerate(data):
        if d == 1:
            graph[i].append(j)
unions = [i for i in range(n)]
q = deque()
for i in range(n):
    visited = [0] * n
    for node in graph[i]:
        q.append(node)
    while q:
        now = q.popleft()
        unions[now] = unions[i]
        visited[now] = 1
        for node in graph[now]:
            if not visited[node]:
                q.append(node)

plans = set(map(int, input().split()))
result = True
for plan in plans:
    if unions[plan] != unions[0]:
        result = False
        break
if result:
    print("YES")
else:
    print("NO")