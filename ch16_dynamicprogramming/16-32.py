# 정수 삼각형
n = int(input())
triangle = []
max_array = []
result = 0
for i in range(n):
    triangle.append(list(map(int, input().split())))
    max_array.append([0] * (i + 1))
# 초기값 설정
max_array[0][0] = triangle[0][0]
if n == 1:
    print(triangle[0][0])
else:
    dx = [1, 1]
    dy = [0, 1]
    for i in range(n):
        for j, number in enumerate(triangle[i]):
            for k in range(2):
                nx = i + dx[k]
                ny = j + dy[k]
                if nx < n and ny <= i + 1:
                    max_array[nx][ny] = max(max_array[nx][ny], max_array[i][j] + triangle[nx][ny])
                    result = max(result, max_array[nx][ny]) 
    print(result)