# 캐릭터 이동
# 맵 외곽으로 나가는 것은 고려하지 않는다.
n, m = map(int, input().split())
x, y, direction = map(int, input().split())
result = 0
terrain = []
checked = [[0] * m for _ in range(n)]
checked[x][y] = 1
for _ in range(n):
    terrain.append(list(map(int, input().split())))


dx = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def turn_left():
    global next_direction
    next_direction += -1
    if ( next_direction < 0 ):
         next_direction += 4


while True:
    # 캐릭터의 위치가 바다라면 종료
    if ( terrain[x][y] == 1):                                
        result -= 1
        break
    print(x, y)
    next_direction = direction 
    # 다음 방향 탐색
    for _ in range(4):                                       
        turn_left()
        nx = x + dx[next_direction][0]
        ny = y + dx[next_direction][1]
        # 이동성공 시 위치, 방향, checked 배열 재설정
        if (terrain[nx][ny] == 0 and checked[nx][ny] == 0):  
            x = nx
            y = ny
            direction = next_direction
            checked[x][y] = 1 
            result += 1
            break
    # 이동실패 시 뒷걸음질
    if ( nx != x or ny != y):                                           
        turn_left()
        turn_left()
        x += dx[next_direction][0]
        y += dx[next_direction][1]
        result += 1
        

print(result)