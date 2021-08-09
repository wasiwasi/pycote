# 못생긴 수
import heapq
n = int(input())
factor = [2, 3, 5]
ugly = [0] * n
index = 0
q = []
heapq.heappush(q, 1)
while not ugly[n - 1]:
    now = heapq.heappop(q)
    if now in ugly:
        continue
    ugly[index] = now
    index += 1
    for f in factor:
        temp = f * now
        if temp not in q:
            heapq.heappush(q, temp)
print(ugly[-1])

# ugly에 있는 수의 2 3 5곱을 저장       * 저장되는 수가 충분히 많아야 정답을 기대할 수 있음
# n = int(input())
# ugly = set([])
# ugly.append(1)
# factor = [2, 3, 5]
# # 2, 3 ,5의 배수를 저장
# # 작은수에 곱함
# index = 0
# while len(ugly) != 5000:
#     for f in factor:
#         temp = ugly[index] * f
#         if temp not in ugly:
#             ugly.append(temp)
#     index += 1
# ugly.sort()
# print(ugly[n - 1])