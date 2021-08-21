# 청소년 상어
import copy
SHARK = 17
n = 4
sea = [[] for _ in range(n)]
fishs = [i for i in range(1, SHARK)]
fish_pos = [0] * 18
directions = [0] * 18
for i in range(n):
    data = list(map(int, input().split()))
    for j, d in enumerate(data[::2]):
        js = [1, 3, 5, 7]
        # 첫번째 물고기를 없애고 상어fish(SHARK)를 넣음
        if i == 0 and j == 0:
            fishs.remove(d)
            sea[i].append(SHARK)
            fish_pos[SHARK] = (i, j)
            directions[SHARK] = data[js[j]]
            result = d
            continue
        sea[i].append(d)
        fish_pos[d] = (i, j)
        directions[d] = data[js[j]]
dx = [0, -1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 0, -1, -1, -1, 0, 1, 1, 1]
def dfs(sea, fish_pos, directions, total):
    global result
    sea = copy.deepcopy(sea)
    fish_pos = copy.deepcopy(fish_pos)
    directions = copy.deepcopy(directions)

    result = max(result, total)
    # 물고기 이동
    for fish in fishs:
        x, y = fish_pos[fish]
        direction = directions[fish]
        flag = 1
        while flag:
            nx = x + dx[direction]
            ny = y + dy[direction]
            if nx >= 0 and nx < n and ny >= 0 and ny < n and sea[nx][ny] != SHARK:
                # 빈칸이라면 물고기 이동
                if sea[nx][ny] == 0:
                    sea[nx][ny] = fish
                    sea[x][y] = 0
                    fish_pos[fish] = (nx, ny)
                # 물고기가 있다면
                else:
                    sea[nx][ny], sea[x][y] = sea[x][y], sea[nx][ny]
                    fish_pos[sea[x][y]], fish_pos[sea[nx][ny]] = fish_pos[sea[nx][ny]], fish_pos[sea[x][y]]
                directions[fish] = direction
                flag = 0
            else:
                direction += 1
                if direction == 9:
                    direction = 1
    # 상어 이동
    x, y = fish_pos[SHARK]
    direction = directions[SHARK]
    for i in range(1,4):
        nx = x + (dx[direction] * i)
        ny = y + (dy[direction] * i)
        if nx >= 0 and nx < n and ny >= 0 and ny < n and sea[nx][ny] != 0:
            prey = sea[nx][ny]
            
            fish_pos[SHARK] = fish_pos[prey]
            directions[SHARK] = directions[prey]
            sea[x][y] = 0
            sea[nx][ny] = SHARK
            fishs.remove(prey)
            dfs(sea, fish_pos, directions, total + prey)
            # 다음 사냥감 탐색
            # 지역변수라 없어도 될듯
            fishs.append(prey)
            fishs.sort()
            sea[nx][ny] = prey
            sea[x][y] = SHARK
            directions[SHARK] = direction
            fish_pos[SHARK] = (x, y)
            
    return 0

dfs(sea, fish_pos, directions, result)
print(result)