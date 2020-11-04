N = int(input())

arr = [list(map(int, input().split())) for _ in range(N)]

dp = [[0] * (i + 1) for i in range(N)]

for n in range(N):
    for j in range(len(arr[n])):
        if n == 0:
            dp[n][j] = arr[n][j]
        else:
            if j == 0:
                dp[n][j] = dp[n - 1][j] + arr[n][j]
            elif j == len(arr[n]) - 1:
                dp[n][j] = dp[n - 1][j - 1] + arr[n][j]
            else:
                dp[n][j] = max(dp[n - 1][j - 1], dp[n - 1][j]) + arr[n][j]


print(max(dp[-1]))