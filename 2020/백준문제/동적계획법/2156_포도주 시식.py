N = int(input())

arr = [int(input()) if i != 0 else 0 for i in range(N + 1)]


def solution():
    dp = [0] * (N + 1)

    dp[1] = arr[1]
    if N == 1:
        print(dp[1])
        return

    dp[2] = arr[1] + arr[2]
    if N == 2:
        print(dp[2])
        return

    for i in range(3, N + 1):
        dp[i] = max(dp[i - 3] + arr[i - 1] + arr[i], dp[i - 1], dp[i - 2] + arr[i])
    print(max(dp))


solution()