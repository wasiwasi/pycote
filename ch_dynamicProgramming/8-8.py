# 효율적인 화폐 구성
n, m = map(int, input().split())
coins = []
for _ in range(n):
    coins.append(int(input()))
d = [10001] * (m + 1)
d[0] = 0

for coin in coins:
    for i in range(coin, m + 1):
        if i % coin == 0:
            d[i] = i // coin
        else:
            d[i] = min(d[i], d[i-coin] + 1)
# 다른방법
# for i in range(n):
#     for j in range(coins[i], m + 1):
#         if d[j - coins[i]] != 10001:
#             d[j] = min(d[j], d[j - coins[i] + 1])


if (d[m] == 10001):
    print("-1")
else:
    print(d[m])
