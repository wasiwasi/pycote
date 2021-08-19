# 아기 상어
from collections import deque

INF = int(1e9)
n = int(input())
shark_size = 2
shark_grow = 0
fishs = []
sea = [[] for _ in range(n)]
for i in range(n):
    data = list(map(int, input().split()))
    for j, d in enumerate(data):
        if d == 9:
            shark_pos = (i, j)
            # sea 배열에는 물고기들만 추가함
            sea[i].append(0)
        else:
            sea[i].append(d)
            if d != 0:
                fishs.append(d)
fishs.sort()

def bfs():
    distance = [[INF] * n for _ in range(n)]
    visited = [[0] * n for _ in range(n)]
    dy = [0, 1, 0, -1]
    dx = [-1, 0, 1, 0]
    
    q = deque()
    q.append(shark_pos)
    # 상어자신의 거리를 0으로 초기화
    distance[shark_pos[0]][shark_pos[1]] = 0
    while q:
        x, y = q.popleft()
        # 방문처리
        visited[x][y] = 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 주위공간이 유효한지 확인
            if nx >= 0 and nx < n and ny >= 0 and ny < n:
                # 미방문이고 상어보다 큰 물고기가 없을 경우(장애물처리) 큐에 넣음
                if visited[nx][ny] == 0 and sea[nx][ny] <= shark_size:
                    q.append((nx, ny))
                    distance[nx][ny] = distance[x][y] + 1               
    return distance

def eat_fish(distance):
    global shark_grow
    global shark_size
    global shark_pos
    global sea
    # 상어자리를 INF로 초기화시켜 가장 가까운 물고기를 찾기 쉽게 함
    distance[shark_pos[0]][shark_pos[1]] = INF
    min_dist = INF
    min_x = 21
    min_y = 21
    for i in range(n):
        for j in range(n):
            # 먹을 수 있는 물고기라면
            if sea[i][j] != 0 and distance[i][j] != INF and sea[i][j] < shark_size:
                # 최소거리라면
                if min_dist > distance[i][j]:
                    min_x = i
                    min_y = j
                    min_dist = distance[min_x][min_y]
    # 먹을 수 있는 물고기가 갇혀있을 경우
    if min_x == 21 and min_y == 21:
        return 0
    # 물고기 삭제
    fishs.remove(sea[min_x][min_y])
    sea[min_x][min_y] = 0
    # 상어 위치를 물고기 위치로 변경
    shark_pos = (min_x, min_y)
    # 상어의 성장확인
    shark_grow += 1
    if shark_grow == shark_size:
        shark_size += 1
        shark_grow = 0

    return distance[min_x][min_y]

count = 0

# fishs는 오름차순으로 정렬되어있어 첫 원소가 작은 물고기라면 먹을 수 있는 상태
while fishs and fishs[0] < shark_size:
    distance = bfs()
    dist = eat_fish(distance)
    if not dist:
        break
    count += dist
                                
print(count)