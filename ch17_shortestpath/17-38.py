# 정확한 순위
INF = int(1e9)
n, m = map(int, input().split())
graph = [[INF] * (n + 1) for _ in range(n + 1)]
# 초기화
for _ in range(n + 1):
    i, j = map(int, input().split())
    graph[i][j] = 1
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i == j:
            graph[i][j] = 0
# 플로이드
for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])


result = 0
for i in range(1, n + 1):
    count = 0
    for j in range(1, n + 1):
        # 방향그래프 이므로 양쪽으로 체크
        if graph[i][j] != INF or graph[j][i] != INF:
            count += 1
    if count == n:
        result += 1
print(result)