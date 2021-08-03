# 인구 이동
from collections import deque

n, l, r = map(int, input().split())
A = []
for i in range(n):
    A.append(list(map(int, input().split())))
result = 0
# 초기 실행을 위해 move_count는 1로 초기화
move_count = 1

# 인접한 국가들중 연합할 국가 선택
def check_boundary(x, y):
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        # 인접국의 좌표가 유효하고 연합에 소속되지 않은 국가일 경우
        if nx >= 0 and nx < n and ny >= 0 and ny < n and not flag[nx][ny]:
            diff = abs(A[x][y] - A[nx][ny])
            # 차이가 범위안에 있다면 큐와 union배열에 추가
            if diff >= l and diff <= r:
                q.append((nx, ny))
                union[union_number].append((nx, ny))
                flag[nx][ny] = 1
        else:
            continue
# 인구이동이 없을 때 까지 반복
while move_count:
    result += 1
    # flag, union, union_number, move_count 초기화
    flag = [[0] * n for _ in range(n)]
    union = [[] for _ in range(n ** 2)]
    union_number = 0
    move_count = 0
    for i in range(n):
        for j in range(n):
            q = deque()
            # 이미 체크한 좌표인지 확인 (이미 소속된 국가를 재탐색하는 것을 막기 위함)
            if not flag[i][j]:
                q.append((i, j))
                union[union_number].append((i, j))
                flag[i][j] = 1
            else:
                continue
            # 큐에서 값을 빼며 국경체크(bfs)진행, 큐가 끝났다면 연합번호를 1 증가함
            while q:
                x, y = q.popleft()
                check_boundary(x, y)
            union_number += 1
    # 인구이동 실행
    for countries in union:
        if len(countries) > 1:
            move_count += 1
            total = 0
            for x, y in countries:
                total += A[x][y]
            new_population = total // len(countries)
            for x, y in countries:
                A[x][y] = new_population
            
print(result - 1)
                       