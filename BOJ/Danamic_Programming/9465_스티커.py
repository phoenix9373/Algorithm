import sys


for tc in range(int(sys.stdin.readline())):
    N = int(input())
    arr = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(2)]

    dp = [[0] * N for _ in range(2)]

    for j in range(N):
        for i in range(2):
            if j == 0:
                dp[i][j] = arr[i][j]
            elif j == 1:
                dp[i][j] = arr[i][j] + arr[(i + 1) % 2][j - 1]
            else:
                dp[i][j] = max(dp[(i + 1) % 2][j - 1], dp[(i + 1) % 2][j - 2]) + arr[i][j]
    print(max(dp[0][N - 1], dp[1][N - 1]))