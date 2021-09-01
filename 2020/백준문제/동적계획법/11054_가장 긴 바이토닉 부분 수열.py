N = int(input())

arr = list(map(int, input().split()))


def solution(seq):
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
    return dp


res1 = solution(arr)
res2 = solution(arr[::-1])[::-1]

result = [i + j - 1 for i, j in zip(res1, res2)]
print(max(result))