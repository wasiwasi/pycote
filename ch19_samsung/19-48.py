# 어른 상어
N, M, k = map(int, input().split())
# 상어의 좌표와 전체 리스트 초기화
sea = []
sharks = []
shark_pos = [0] * (M + 1)
for i in range(N):
    data = list(map(int, input().split()))
    sea.append(data)
    for j, d in enumerate(data):
        if d != 0:
            shark_pos[d] = (i, j)
            sharks.append(d)
sharks.sort()
# 방향 초기화
shark_direction = [0] * (M + 1)
for i, d in enumerate(list(map(int, input().split())), start = 1):
    shark_direction[i] = d
# 상어 우선순위 초기화
priority = [[[[], []] for _ in range(5)] for _ in range(M + 1)] # 상어번호, 방향, [dx, dy]순으로 이동 우선순위를 가진 리스트
for m in range(1, M + 1):
    for i in range(1, 5):
        data = list(map(int, input().split()))
        for d in data:
            if d == 1:
                priority[m][i][0].append(-1)
                priority[m][i][1].append(0)
            elif d == 2:
                priority[m][i][0].append(1)
                priority[m][i][1].append(0)
            elif d == 3:
                priority[m][i][0].append(0)
                priority[m][i][1].append(-1)
            elif d == 4:
                priority[m][i][0].append(0)
                priority[m][i][1].append(1)
direction_dict = {(-1, 0) : 1, (1, 0) : 2, (0, -1) : 3, (0, 1) : 4}
# sharsk의 길이가 1이 될때까지(1만남음) 반복
count = 0
stink = [[0] * N for _ in range(N)] # [상어번호, 남은시간]을 가진 2차원 리스트

def out(shark):
    x, y = shark_pos[shark]
    sea[x][y] = 0
    shark_pos[shark] = 0
    return 0

def move(shark, direction, nx, ny):
    x, y = shark_pos[shark]
    sea[x][y] = 0
    sea[nx][ny] = shark
    shark_pos[shark] = (nx, ny)
    shark_direction[shark] = direction
    return 0

def check_pos(shark, dx, dy):
    x, y = shark_pos[shark]
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >= 0 and nx < N and ny >= 0 and ny < N:
            # 아무 냄새가 없는지 확인
            if stink[nx][ny] == 0:
                if sea[nx][ny] == 0:
                    move(shark, direction_dict[(dx[i], dy[i])], nx, ny)
                    return 0 
                # 이미 자리잡은 상어가 있다면
                else:
                    out(shark)
                    return shark 
    # 빈칸이 없다면 자신의 냄새방향으로 감
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >= 0 and nx < N and ny >= 0 and ny < N:
            # 자기 냄새가 나는 칸이라면 이동
            if stink[nx][ny][0] == shark:
                move(shark, direction_dict[(dx[i], dy[i])], nx, ny)
                return 0
    return 0

while len(sharks) != 1:
    if count == 1000:
        count = -1
        break 
    # 냄새를 남김
    for shark in sharks:
        x, y = shark_pos[shark]
        stink[x][y] = [shark, k]
    # 상어이동
    # out함수에서 바로 sharks삭제시 for문이 중단되기때문에 out_shark를 이용해 나중에 일괄적으로 빼줌
    out_shark = []
    for shark in sharks:
        direction = shark_direction[shark]
        out_shark.append(check_pos(shark, priority[shark][direction][0], priority[shark][direction][1]))
    for shark in out_shark:
        if shark != 0:
            sharks.remove(shark)
    # 시간이 가고 냄새가 줄어듬
    count += 1
    for i, row in enumerate(stink):
        for j, space in enumerate(row):
            if space:
                space[1] -= 1
                if space[1] == 0:
                    stink[i][j] = 0
print(count)