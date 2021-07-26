# 문자열 뒤집기
s = input()
# 연속된 숫자를 하나의 묶음으로 치환해 개수를 셈
count = [0] * 2

# 첫번째 비트 확인
if int(s[0]) == 0:
    count[0] += 1
    memory = 0
else:
    count[1] += 1
    memory = 1 

for bit in s[1:]:
    bit = int(bit)
    # 변화가 있을 시 개수 증가
    if bit != memory:
        memory = bit
        count[bit] += 1

print(min(count[0], count[1]))
