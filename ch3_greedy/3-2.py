# -*- coding: UTF-8 -*-
# 큰 수의 법칙
n, m, k = map(int, input().split())

data = list(map(int, input().split()))

data.sort()
first = data[-1]
second = data[-2]
result = 0

# count = m // (k+1)
# remain = m % (k+1)
count, remain = divmod(m, k+1)

result += count * second
result += count * k * first
result += remain * first

print(result)