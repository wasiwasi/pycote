# 두 배열의 원소 교체

n, k = map(int, input().split())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort()

for i in range(k):
    if a[i] < b[n-i-1]:
        a[i], b[n-i-1] = b[n-i-1], a[i]
    else:
        break

print(sum(a))
