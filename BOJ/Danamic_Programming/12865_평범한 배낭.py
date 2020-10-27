N, K = map(int, input().split())

arr = [[0, 0]] + sorted([list(map(int, input().split())) for _ in range(N)])

dp = [[0 for _ in range(K + 1)] for _ in range(N + 1)]

for i in range(1, N + 1):
    for j in range(1, K + 1):
        if arr[i][0] <= j:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - arr[i][0]] + arr[i][1])
        else:
            dp[i][j] = dp[i - 1][j]

print(dp[N][K])