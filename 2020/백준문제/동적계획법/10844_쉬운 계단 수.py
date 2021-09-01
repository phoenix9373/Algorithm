N = int(input())

dp = [[0] * 10 for _ in range(N + 1)]
dp[1] = [0] + [1] * 9

if N > 1:
    for n in range(2, N + 1):
        for i in range(10):
            if i == 0:
                dp[n][i] = dp[n - 1][i + 1]
            elif i == 9:
                dp[n][i] = dp[n - 1][i - 1]
            else:
                dp[n][i] = dp[n - 1][i + 1] + dp[n - 1][i - 1]
res = sum(dp[N]) % pow(10, 9)
print(res)