N = int(input())

dp = [[0] * 10 for _ in range(N + 1)]

for i in range(N + 1):
    for j in range(10):
        if i == 1:
            dp[i][j] = 1
        elif i > 1:
            dp[i][j] = sum(dp[i - 1][j:])
res = sum(dp[N]) % 10007
print(res)