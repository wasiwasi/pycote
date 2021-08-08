# 금광
T = int(input())
n = [0 for _ in range(T)]
m = [0 for _ in range(T)]
data = [0 for _ in range(T)]
result = [0 for _ in range(T)]
for time in range(T):
    n[time], m[time] = map(int, input().split())
    data[time] = list(map(int, input().split()))

for time in range(T):
    mine = [[] for _ in range(n[time])]
    storage = [[0] * m[time] for _ in range(n[time])]
    for i in range(n[time]):
        for j in range(m[time]):
            mine[i].append(data[time][(i * m[time]) + j])
            if j == 0:
                storage[i][j] = data[time][(i * m[time]) + j]
    dx = [-1, 0, 1]
    dy = [1, 1, 1]
    for j in range(m[time]):
        for i in range(n[time]):
            for k in range(3):
                next_i = i + dx[k]
                next_j = j + dy[k]
                if next_i >= 0 and next_i < n[time] and next_j >= 0 and next_j < m[time]:
                    storage[next_i][next_j] = max(storage[next_i][next_j], storage[i][j] + mine[next_i][next_j])
                    result[time] = max(result[time], storage[next_i][next_j])
for r in result:
    print(r)