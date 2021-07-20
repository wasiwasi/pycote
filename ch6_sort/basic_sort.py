import time

array = [7, 5, 3, 4, 5, 1, 9, 6, 8, 2]

#선택
# for i in range(len(array)):
#     min_index = i
#     for j in range(i+1, len(array)):
#         if array[min_index] > array[j]:
#             min_index = j
#     array[i], array[min_index] = array[min_index], array[i]
# print(array)

# 삽입
# for i in range(1, len(array)):
#     for j in range(i, 0, -1):
#         if array[j-1] > array[j]:
#             array[j-1], array[j] = array[j], array[j-1]
#         else: break
# print(array)

# 퀵
# def quick_sort(array):
#     if len(array) <= 1:
#         return array
    
#     pivot = array[0]
#     tail = array[1:]

#     left_side = [x for x in tail if x <= pivot]
#     right_side = [x for x in tail if x > pivot]

#     return quick_sort(left_side) + [pivot] + quick_sort(right_side)
# print(quick_sort(array))

#계수
# count = [0] * (max(array)+1)

# for i in range(len(array)):
#     count[array[i]] += 1

# for i in range(len(count)):
#     for j in range(count[i]):
#         print(i, end = ' ')