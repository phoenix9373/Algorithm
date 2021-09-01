N = int(input())

seq = list(map(int, input().split()))
dp = [0] * N

for i in range(N):
    if i == 0:
        dp[i] = 1
        continue

    tmp = 0

    for j in range(i - 1, -1, -1):
        if seq[j] < seq[i] and dp[j] > tmp:
            tmp = dp[j]
    dp[i] = tmp + 1

print(max(dp))