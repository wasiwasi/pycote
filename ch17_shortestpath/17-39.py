# 화성탐사
import heapq

INF = int(1e9)

def dijkstra(n, space, distance):
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]
    q = []
    heapq.heappush(q, (space[0][0], 0, 0))
    
    while q:
        dist, x, y = heapq.heappop(q)
        if distance[x][y] < dist:
            continue
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= 0 and nx < n and ny >= 0 and ny < n:
                cost = dist + space[nx][ny]                
                if cost < distance[nx][ny]:
                    distance[nx][ny] = cost
                    heapq.heappush(q, (cost, nx, ny))
            else:
                continue

    
    return distance[n-1][n-1]

T = int(input())
ns = []
spaces = []
distances = []
for t in range(T):
    ns.append(int(input()))
    spaces.append([[] for _ in range(ns[t])])
    for i in range(ns[t]):
        spaces[t][i] = list(map(int, input().split()))
    distances.append([[INF] * ns[t] for _ in range(ns[t])])

for t in range(T):
    print(dijkstra(ns[t], spaces[t], distances[t]))