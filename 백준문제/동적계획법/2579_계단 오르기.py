N = int(input())
stairs = [int(input()) for _ in range(N)]

dp = [0] * N

for i in range(N):
    if i == 0:
        dp[i] = stairs[0]
    elif i == 1:
        dp[i] = dp[i - 1] + stairs[i]
    elif i == 2:
        dp[i] = max(stairs[i - 1], stairs[i - 2]) + stairs[i]
    else:
        dp[i] = max(dp[i - 2], dp[i - 3] + stairs[i - 1]) + stairs[i]

print(dp[-1])
