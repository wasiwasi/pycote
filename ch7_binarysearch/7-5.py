# 부품찾기
def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        elif array[mid] < target:
            start = mid + 1
    return None

n = int(input())
array = list(map(int, input().split()))

m = int(input())
targets = list(map(int, input().split()))


for target in targets:
    result = binary_search(array, target, 0, n-1)
    if result == None:
        print("No", end = ' ')
    else :
        print("Yes", end = ' ')

# set을 이용한 방법
# n = int(input())
# array = set(map(int, input().split()))

# m = int(input())
# targets = list(map(int, input().split()))

# for target in targets:
#     if target in array:
#         print("yes", end = ' ')
#     else:
#         print("no", end = ' ')