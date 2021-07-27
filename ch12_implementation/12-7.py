# 럭키 스트레이트
n = input()

mid = len(n) // 2

left = 0
right = 0

for number in n[:mid]:
    left += int(number)

for number in n[mid:]:
    right += int(number)

if left == right:
    print("LUCKY")
else:
    print("READY")