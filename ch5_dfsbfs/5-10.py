# 음료수 얼려 먹기

n, m = map(int, input().split())

graph = []
result = 0

for _ in range(n):
    graph.append(list(map(int, input())))

def dfs(i, j):
    if i < 0 or i > n-1 or j < 0 or j > m-1:
        return False
    
    if graph[i][j] == 0:
        graph[i][j] = 1
        dfs(i-1, j)
        dfs(i, j+1)
        dfs(i+1, j)
        dfs(i, j-1)

        return True
    
    return False

for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            result += 1

print(result)