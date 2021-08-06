# 연산자 끼워넣기
from itertools import permutations

n = int(input())
numbers = list(map(int, input().split()))
operators = list(map(int, input().split()))
all_operators = []
for i in range(4):
    while operators[i]:
        operators[i] -= 1
        if i == 0:
            all_operators.append('+')
        elif i == 1:
            all_operators.append('-')
        elif i == 2:
            all_operators.append('*')
        else:
            all_operators.append('//')
candidate = set(permutations(all_operators, n - 1))
max_value = -987654321
min_value = 987654321

for ops in candidate:
    temp = 0
    stack = []
    for i in range(n):
        stack.append(str(numbers[i]))
        # 스택이 숫자 연산자 숫자 형태일때
        if len(stack) == 3:
            # 피제수(나누어지는 수)가 음수라면 변환을 거치고, 보통의 상황에서는 연산진행
            if stack[1] == '//' and int(stack[0]) < 0 :
                temp = -int(stack[0]) // int(stack[2])
                stack = [str(temp)]
            else:
                temp = eval("".join(stack))
                stack = [str(temp)]
        # ops는 n보다 1작기 때문에 마지막루프에서는 작동을 안해야함
        if i != (n - 1):
            stack.append(ops[i])
    result = int(stack.pop())
    max_value = max(max_value, result)
    min_value = min(min_value, result)

print(max_value)
print(min_value)
    