# 곱하기 혹은 더하기
s = input()
result = 0

for number in s:
    number = int(number)
    if result == 0 or number <= 1:
        result += number
        continue
    else:
        result *= number

print(result)