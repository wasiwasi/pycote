# 볼링공 고르기
n, m = map(int, input().split())
k = list(map(int, input().split()))
result = 0

# for i, weight in enumerate(k):
#     for j in k[i + 1:]:
#         #두 공의 무게가 같으면 패스
#         if weight == j:
#             continue
#         result += 1

# print(result)

array = [0] * 11
for x in k:
    array[x] += 1

for i in range(1, m + 1):
    n -= array[i]
    result += array[i] * n

print(result)