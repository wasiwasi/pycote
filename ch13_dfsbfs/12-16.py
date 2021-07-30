# 바이러스
from itertools import product, combinations
import copy
import time

def virus(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx >= 0 and nx < n and ny >= 0 and ny < m:
            if temp[nx][ny] == 0:
                temp[nx][ny] = 2
                virus(nx, ny)

dx = [-1, 0, 1, 0]
dy = [0, 1, 0 ,-1]
n, m = map(int, input().split())
default_state = [([0] * m) for _ in range(n)]
result = 0

for i in range(n):
    data = list(map(int, input().split()))
    for j, d in enumerate(data):
        if d == 0:
            continue
        else:
            default_state[i][j] = d

starttime = time.time()
indexi = [i for i in range(n)]
indexj = [j for j in range(m)] 
indexij = list(product(indexi, indexj))
situation = list(combinations(indexij, 3))

for situ in situation:
    temp = copy.deepcopy(default_state)
    count = 0
    # 벽 추가
    for wall_x, wall_y in situ:
        # 벽과 바이러스의 위치가 겹치면 x
        if temp[wall_x][wall_y] == 2:
            break
        temp[wall_x][wall_y] = 1

    # 바이러스 전파
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 2:
                virus(i, j)
    # 0의 개수 카운트
    for t in temp:
        count += t.count(0)
    result = max(result, count)

print(result)
print(time.time() - starttime)