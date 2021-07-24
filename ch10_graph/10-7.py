# 팀 결성
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] =  find_parent(parent, parent[x])
    return  parent[x]

def union_team(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

def check_team(parent, a, b):
    if parent[a] == parent[b]:
        print("YES")
    else:
        print("NO")

n, m = map(int, input().split())
parent = [0] * (n + 1)

for _ in range(m):
    command, a, b = map(int, input().split())

    if command == 0:
        union_team(parent, a, b)
    else:
        check_team(parent, a, b)