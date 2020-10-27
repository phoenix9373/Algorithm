N = int(input())
scores = [int(input()) for _ in range(N)]
DP = [0] * N


def dp(arr, dp_arr, n):
    dp_arr[0] = arr[0]
    dp_arr[1] = max(arr[0] + arr[1], arr[1])
    dp_arr[2] = max(arr[1] + arr[2], arr[0] + arr[2])

    if n > 3:
        for i in range(3, n):
            dp_arr[i] = max(dp_arr[i - 3] + arr[i - 1] + arr[i], dp_arr[i - 2] + arr[i])

    return dp_arr[-1]


res = dp(scores, DP, N - 1)
print(res)
