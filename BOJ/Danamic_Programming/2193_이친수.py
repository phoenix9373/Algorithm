N = int(input())

dp = [[0] * 2 for _ in range(N + 1)]
dp[1][1] = 1
if N > 1:
    dp[2][0], dp[2][1] = 2, 1
if N > 2:
    for i in range(3, N + 1):
        for j in range(2):
            if j == 1:
                dp[i][j] = dp[i - 1][0]
            else:
                dp[i][j] = sum(dp[i - 1])
print(dp[N][1])