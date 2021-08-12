# 탑승구
G = int(input())
P = int(input())
planes = []
for _ in range(P):
    planes.append(int(input()))
remain_space = G
remain_plane = P
hangar = 1
result = 0
for i in range(P):
    if not remain_space or not remain_plane:
        break
    if planes[i] >= hangar:
        remain_plane -= 1
        remain_space -= 1
        hangar += 1
        result += 1
    else:
        break
print(result)