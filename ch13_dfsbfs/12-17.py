# 경쟁적 전염
from collections import deque

n, k = map(int, input().split())
test_tube = [[0] * n for _ in range(n)]
# 각 바이러스의 좌표를 갖고 있는 배열
virus_pos = []
for i in range(n):
    data = list(map(int, input().split()))        
    # 바이러스라면 바이러스위치를 추가
    for j, d in enumerate(data):
        if d != 0:
            test_tube[i][j] = d
            virus_pos.append((d, 0, i, j))
s, x, y = map(int, input().split())
virus_pos.sort()

q = deque()
for v in virus_pos:
    q.append(v)
# 바이러스의 이동을 상하좌우 배열로 표현
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

while q:
    virus, time, vx, vy = q.popleft()
    if time == s:
        break
    for i in range(4):
        # next 좌표를 생성
        nx = vx + dx[i]
        ny = vy + dy[i]
        # 다음 좌표가 유효하다면
        if nx >= 0 and nx < n and ny >= 0 and ny < n:
            # 무결한 곳(0)이라면 전염시킴
            if test_tube[nx][ny] == 0:
                test_tube[nx][ny] = virus
                # 큐에 새로운 바이러스의 위치, 시간 + 1을 넣음
                q.append((virus, time + 1, nx, ny))

print(test_tube[x - 1][y - 1])