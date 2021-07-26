# 만들 수 없는 금액
n = int(input())
coins = list(map(int, input().split()))
coins.sort(reverse = True)
number = 0

while True:
    number += 1
    sum = 0

    for coin in coins:
        if sum + coin <= number:
            sum += coin
    
    if sum != number:
        print(number)
        break