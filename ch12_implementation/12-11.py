# 뱀
from collections import deque

res = 0
n = int(input())
k = int(input())
apples = []
for _ in range(k):
    apples.append(tuple(map(int, input().split())))

l = int(input())
ops = []
for _ in range(l):
    ops.append(map(str, input().split()))

# 오른쪽, 아래, 왼쪽, 위
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
direction = 0

# 루프 탈출
game_end = 0

q = deque()
q.append((1, 1))

prev_time = 0

for time, op in ops:
    time = int(time)
    for _ in range(time - prev_time):
        res += 1
        now = q[-1]
        next_pos = (now[0] + dx[direction], now[1] + dy[direction])
        # 자기 몸이나 벽에 충돌
        if next_pos in q or next_pos[0] < 1 or next_pos[0] >= n + 1 or next_pos[1] < 1 or next_pos[1] >= n + 1 :
            game_end = 1
            break
        # 이동한곳에 사과가 있다면 사과로 머리이동
        elif next_pos in apples:
            apples.remove(next_pos)
            q.append(next_pos)
        # 빈공간이라면 머리를 이동하고 꼬리를 자름
        else:
            q.append(next_pos)
            q.popleft()
    prev_time = time
    if game_end == 1:
        break
    if op == 'L':
        direction -= 1
        if direction == -1:
            direction = 3
    else:
        direction += 1
        if direction == 4:
            direction = 0

now = q[-1]
next_pos = (now[0] + dx[direction], now[1] + dy[direction])

# 아직 게임이 끝나지 않았다면 끝날때 까지 진행
if not game_end:
    while True:
        res += 1
        if next_pos in q or next_pos[0] < 1 or next_pos[0] + 1 >= n or next_pos[1] < 1 or next_pos[1] >= n + 1 :
            break
        elif next_pos in apples:
            q.append(next_pos)
        else:
            q.append(next_pos)
            q.popleft()
        now = q[-1]
        next_pos = (now[0] + dx[direction], now[1] + dy[direction])

print(res)  