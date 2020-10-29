# 1. DP
for tc in range(1, int(input()) + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    dp = [[0] * N for _ in range(N)]
    dp[0][0] = arr[0][0]

    for i in range(N):
        for j in range(N):
            if i == 0 and j > 0:
                dp[i][j] = dp[i][j - 1] + arr[i][j]
            elif i > 0 and j == 0:
                dp[i][j] = dp[i - 1][j] + arr[i][j]
            else:
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + arr[i][j]

    print('#{} {}'.format(tc, dp[N - 1][N - 1]))

# 2. 완전검색
# di = [1, 0]
# dj = [0, 1]
#
#
# def dfs(v, res):
#     global ans
#     if res >= ans:
#         return
#
#     i, j = v[0], v[1]
#     visited[i][j] = 1
#
#     if i == N - 1 and j == N - 1:
#         if res < ans:
#             ans = res
#
#     for k in range(2):
#         ni = i + di[k]
#         nj = j + dj[k]
#         if 0 <= ni < N and 0 <= nj < N and visited[ni][nj] == 0:
#             dfs([ni, nj], res + arr[ni][nj])
#             visited[ni][nj] = 0
#
#
# for tc in range(1, int(input()) + 1):
#     N = int(input())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#     visited = [[0] * N for _ in range(N)]
#     ans = pow(2, 30)
#
#     dfs([0, 0], arr[0][0])
#
#     print('#{} {}'.format(tc, ans))