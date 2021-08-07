# 고정점 찾기
def binary_search(array, start, end):
    mid = (start + end) // 2
    if start > end:
        return -1
    if array[mid] == mid:
        return mid
    elif array[mid] > mid:
        return binary_search(array, start, mid -1)
    elif array[mid] < mid:
        return binary_search(array, mid + 1, end)
    return -1

n = int(input())
array = list(map(int, input().split()))

print(binary_search(array, 0, n - 1))
