# 도시 분할 계획
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


n, m = map(int, input().split())
parent = [0] * (n + 1)
edges = []
total = 0

for i in range(1, n + 1):
    parent[i] = i

for _ in range(m):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))

edges.sort()
secondTown = 0

for edge in edges:
    cost, a, b = edge
    if find_parent(parent, a) == find_parent(parent, b):
        continue
    else:
        union_parent(parent, a, b)
        total += cost
        last = cost

print(total-last)