# 무지의 먹방 라이브

# 기본답
# def search_index(food_times, index):
#     while food_times[index] == 0:
#         index += 1
    
#     return index % len(food_times)

# def solution(food_times, k):
#     answer = 0
    
#     i = 0
#     for _ in range(k):
#         if food_times[i] != 0:
#             food_times[i] -= 1
#             i += 1
#         else:
#             i = search_index(food_times, i)
#             food_times[i] -= 1
#             i += 1
#         i = i % len(food_times)
    
#     answer = i + 1
#     return answer

# 최적화 실패
# def search_index(food_times, index):
#     while food_times[index] == 0:
#         index = (index + 1) % len(food_times)
    
#     return index 

# def optimize_array(food_times, k):
#     surplus = 0
#     cycle = k // len(food_times)
#     for i in range(len(food_times)):
#         food_times[i] -= cycle
#         if food_times[i] < 0:
#             surplus -= food_times[i]
#             food_times[i] = 0
#     return cycle, surplus

# def solution(food_times, k):
#     answer = 0
#     i = 0
#     total = sum(food_times)
#     while total > k and len(food_times) < k:
#         cycle, surplus = optimize_array(food_times, k)
#         k = (k % len(food_times)) + surplus
#         total = sum(food_times)
#         # i = surplus % len(food_times)
#     for _ in range(k):
#         if total == 0:
#             break
            
#         if food_times[i] > 0:
#             food_times[i] -= 1
#             i += 1
#             total -= 1
#         else:
#             i = search_index(food_times, i)
#             food_times[i] -= 1
#             i += 1
#             total -= 1
#         i = i % len(food_times)
    
#     if total == 0:
#         answer = -1
#     else:
#         answer = i + 1
#     return answer

# 답
import heapq

def solution(food_times, k):
    if sum(food_times) <= k:
        return -1

    q = []
    for i in range(len(food_times)):
        heapq.heappush(q, (food_times[i], i + 1))

    sum_value = 0
    previous = 0

    length = len(food_times)

    # sum_value + ( 현재의 음식시간 - 이전 음식시간 ) * 현재 음식 개수와 k 비교
    while sum_value + ((q[0][0] - previous) * length) <= k:
        now = heapq.heappop(q)[0]
        sum_value += (now - previous) * length
        length -= 1
        previous = now
    result = sorted(q, key = lambda x: x[1])
    return result[(k - sum_value) % length][1]