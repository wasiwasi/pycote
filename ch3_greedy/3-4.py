# -*- coding: UTF-8 -*-
# 1이 될때 까지

n, k = map(int, input().split())

result = 0

while True:
    if n == 1:
        break
    
    if n % k == 0:
        n //= k
        result += 1
    else:
        n -= 1
        result += 1
print(result)

#예시답안
# n, k = map(int, input().split())
# result = 0

# while True:                   
#     target = (n // k) * k         # 배수로 만들어 값에서 빼주면 빼기수행횟수가 나옴
#     result += (n - target)
#     n = target

#     if n < k:
#         break
#     result += 1
#     n //= k

# result += (n - 1)
# print(result)