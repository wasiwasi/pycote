# 실패율
N = 5
stages = [2, 1, 2, 6, 2, 4, 3, 3]
answer = []
failure = [[] for _ in range(N + 2)]
percentage = []
for person in stages:
    if failure[person]:
        failure[person] += 1
    else:
        failure[person] = 1
for i, count in enumerate(failure[1:]):
    if i == N:
        break
    if count:
        total = 0
        for number in failure[i + 1:]:
            if number:
                total += number
        percentage.append((i + 1, count / total))
    else:
        percentage.append((i + 1, 0))
percentage.sort(key = lambda x: (-x[1], x[0]))
for stage in percentage:
    print(stage[1])
    answer.append(stage[0])
print(answer)