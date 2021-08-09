# 퇴사

n = int(input())
t = []
p = []
dp = [0] * (n + 1)
max_value = 0

for _ in range(n):
    x, y = map(int, input().split())
    t.append(x)
    p.append(y)

for i in range(n - 1, -1, -1):
    time = t[i] + i
    if time <= n:
        dp[i] = max(p[i] + dp[time], max_value)
        max_value = dp[i]
    else:
        dp[i] = max_value
print(max_value)
# n = int(input())
# schedule = []
# dp = []
# outdate = 0
# result = 0
# for k in range(n):
#     data = tuple(map(int, input().split()))
#     # 기한이 초과되는 일정은 애초에 배열에 넣지 않음
#     if (k + 1) + data[0] <= n + 1:
#         schedule.append(data)
#         dp.append(data)
#         result = max(result, data[1])
#     else:
#         outdate += 1
#         continue
# for k in range(n - outdate):
#     now_time = dp[k][0]
#     now_profit = dp[k][1]
#     for i in range(k + schedule[k][0], n - outdate):
#         total_time = schedule[i][0] + now_time
#         total_profit = now_profit + schedule[i][1]
#         if total_time >= 0 and total_time <= n and total_profit > dp[i][1]:
#             dp[i] = (total_time, total_profit)
#             result = max(result, total_profit)
# print(result)