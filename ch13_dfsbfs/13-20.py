# 감시 피하기
n = int(input())
hallway = []
temp = [['X'] * n for _ in range(n)]
for _ in range(n):
    hallway.append(list(map(str, input().split())))
result = "NO"
# 선생님의 경로에 학생이 있나 체크
def find_student(x, y):
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        # 유효한 자리인지 확인
        while nx >= 0 and nx < n and ny >= 0 and ny < n:
            # 장애물이 있다면 그쪽 경로는 중지
            if temp[nx][ny] == 'O':
                break
            # 학생과 마주쳤다면 True 반환
            elif temp[nx][ny] == 'S':
                return True
            nx = nx + dx[i]
            ny = ny + dy[i]
    return False            

def dfs(obstacle):
    global result
    # 장애물 설치가 끝났다면
    if obstacle == 3:
        count_t = 0
        avoid = 0
        # 보드를 temp에 복사
        for i in range(n):
            for j in range(n):
                temp[i][j] = hallway[i][j]
            # print(temp[i]) # 성공한 보드를 
        # 순회하며 선생의 좌표에서 find_student
        for i in range(n):
            for j in range(n):
                if temp[i][j] == 'T':
                    # 선생카운트를 1 증가
                    count_t += 1
                    if not find_student(i, j):
                        # 학생을 찾을 수 없었다면 회피횟수 1 증가
                        avoid += 1
        # 모든 선생이 학생을 찾지 못했다면 YES
        if count_t == avoid:
            result = "YES"
            return 0 

    else:
        for i in range(n):
            for j in range(n):
                if hallway[i][j] == 'X':
                    hallway[i][j] = 'O'
                    obstacle += 1
                    dfs(obstacle)
                    # result가 YES라는 것은 모든 선생이 학생을 찾지 못한 경우가 발생했다는 뜻과 같으므로 탐색 중단
                    if result == "YES":
                        return 0
                    hallway[i][j] = 'X'
                    obstacle -= 1
dfs(0)
print(result)