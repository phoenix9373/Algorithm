N = int(input())
arr = list(map(int, input().split()))

if N == 0:
    print(0)

dp = [0] * N

for i in range(N):
    if i == 0:
        dp[i] = arr[i]
        continue
    if arr[i] < 0 and dp[i - 1] < 0:
        dp[i] = max(arr[i], dp[i - 1])
    else:
        dp[i] = max(arr[i], dp[i - 1] + arr[i])

print(max(dp))