# 경쟁적 전염

n, k = map(int, input().split())
test_tube = [[0] * (n + 1) for _ in range(n + 1)]
# 각 바이러스의 좌표를 갖고 있는 배열
virus_pos = [[] * (n + 1) for _ in range(k + 1)]
for i in range(1, n + 1):
    data = list(map(int, input().split()))
    # 각 좌표에 입력받은 값 대입
    for j, d in enumerate(data):
        test_tube[i][j + 1] = d
        # 바이러스라면 바이러스위치를 추가
        if d != 0:
            virus_pos[d].append((i, j + 1))
s, x, y = map(int, input().split())

# 바이러스의 이동을 상하좌우 배열로 표현
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def virus(vx, vy, temp):
    for i in range(4):
        # next 좌표를 생성
        nx = vx + dx[i]
        ny = vy + dy[i]
        # 다음 좌표가 유효하다면
        if nx > 0 and nx <= n and ny > 0 and ny <= n:
            # 무결한 곳(0)이라면 전염시킴
            if test_tube[nx][ny] == 0:
                test_tube[nx][ny] = virusnumber
                # 바로 virus_pos에 넣으면 갱신된 상태도 바이러스가 전염되기 때문에 temp 배열을 사용
                # 큐를 사용한다면 깔끔하게 구현가능할 듯 
                temp[virusnumber].append((nx, ny))

for _ in range(s):
    temp = [[] * (n + 1) for _ in range(k + 1)]
    for virusnumber, viruses in enumerate(virus_pos):
        for vx, vy in viruses:
            virus(vx, vy, temp)
    # 새로생긴 바이러스의 위치를 virus_pos에 넣어줌
    for i in range(1, k + 1):
        virus_pos[i].extend(temp[i])

print(test_tube[x][y])