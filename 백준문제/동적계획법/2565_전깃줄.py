N = int(input())

arr = sorted([list(map(int, input().split())) for _ in range(N)], key=lambda x: x[0])

dp = [0] * N

for i in range(N):
    if i == 0:
        dp[i] = 1

    tmp = 0

    for j in range(i - 1, -1, -1):
        if arr[i][1] > arr[j][1]:
            if tmp < dp[j]:
                tmp = dp[j]
    dp[i] = tmp + 1

print(N - max(dp))