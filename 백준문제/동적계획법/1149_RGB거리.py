# N은 1000까지.
import sys

N = int(sys.stdin.readline().strip())

arr = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]

dp = [[0] * 3 for _ in range(N)]

for n in range(N):
    for j in range(3):
        if n == 0:
            dp[n][j] = arr[n][j]
        else:
            dp[n][j] = min(dp[n-1][(j+1)%3], dp[n-1][(j+2)%3]) + arr[n][j]

print(min(dp[-1]))