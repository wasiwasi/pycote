# 카드 정렬하기
import heapq
n = int(input())
heap = []
total = 0
for _ in range(n):
    heapq.heappush(heap, int(input()))
while len(heap) != 1:
    temp = heapq.heappop(heap) +  heapq.heappop(heap) 
    heapq.heappush(heap, temp)
    total += temp
print(total)