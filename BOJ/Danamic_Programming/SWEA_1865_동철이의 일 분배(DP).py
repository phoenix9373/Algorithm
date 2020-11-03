# for t in range(int(input())):
#     n = int(input())
#     m = 1 << n
#     d = [0] * m
#     p = [[*map(lambda x: x * .01, map(int, input().split()))] for _ in range(n)]
#     d[0] = 1
#     for i in range(m):
#         x = bin(i).count('1')
#         for j in range(n):
#             if (1 << j) & i == 0:
#                 d[i | (1 << j)] = max(d[i | (1 << j)], d[i] * p[x][j])
#     print(f'#{t + 1} {d[-1] * 100:.6f}')


T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    M = 1 << N
    dp = [[0.0 for _ in range(M)] for _ in range(N)]

    G = []
    for i in range(N):
        G.append(list(map(float, input().split())))
        for j in range(N):
            G[i][j] = G[i][j] / 100

    for i in range(N):
        dp[0][1 << i] = G[0][i]

    for i in range(1, N):
        for cur in range(1, M):
            if dp[i - 1][cur] == 0:
                continue

            for j in range(N):
                if cur & (1 << j) != 0 or G[i][j] == 0:
                    continue
                next = cur | (1 << j)

                dp[i][next] = max(dp[i][next], dp[i - 1][cur] * G[i][j])
    print("#%d %.6f" % (test_case, dp[N - 1][M - 1] * 100))