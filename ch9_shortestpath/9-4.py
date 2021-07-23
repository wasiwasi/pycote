# 미래 도시
INF = int(1e9)

n, m = map(int, input().split())
graph = [[INF] * (n + 1) for _ in range (n + 1)]

for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            graph[a][b] = 0

for _ in range(1, m + 1):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

x, k = map(int, input().split())

for mid in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][mid] + graph[mid][b])

if graph[1][k] == INF or graph[k][x] == INF:
    print("-1")
else:
    print(graph[1][k] + graph[k][x])