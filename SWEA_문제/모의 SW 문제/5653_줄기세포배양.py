# import sys
#
# sys.stdin = open('input.txt', 'r')

di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]

for tc in range(1, int(input()) + 1):
    N, M, K = map(int, input().strip().split())
    arr = [list(map(int, input().strip().split())) for _ in range(N)]
    maps = [[0] * (K // 2 * 2 + M * 2) for _ in range(K // 2 * 2 + N * 2)]
    created = [[0] * (K // 2 * 2 + M * 2) for _ in range(K // 2 * 2 + N * 2)]
    n, m = len(maps), len(maps[0])

    for i in range(N):
        for j in range(M):
            maps[len(maps) // 2 - N // 2 + i][len(maps[0]) // 2 - M // 2 + j] = arr[i][j]

    for t in range(1, K + 1):

        for i in range(n // 2 - N // 2 - t // 2 - 1, n // 2 + N // 2 + t // 2 + 1, 1):
            tmp = []
            for j in range(m // 2 - M // 2 - t // 2 - 1, m // 2 + M // 2 + t // 2 + 1, 1):
                sub_tmp = []

                if maps[i][j] > 0:
                    continue

                for k in range(4):
                    ni, nj = i + di[k], j + dj[k]
                    if 0 <= ni < n and 0 <= nj < m and maps[ni][nj] != 0:  # index check, cell presence
                        if (t - created[ni][nj]) / maps[ni][nj] > 1:
                            sub_tmp.append([ni, nj])
                maxX = 0
                for X, Y in sub_tmp:
                    if maps[X][Y] > maxX:
                        maxX = maps[X][Y]
                if maxX != 0:
                    tmp.append([i, j, maxX])
                # del sub_tmp

            for x, y, maxK in tmp:
                maps[x][y] = maxK
                created[x][y] = t
            # del tmp

    count = 0
    for i in range(n):
        for j in range(m):
            if maps[i][j] != 0 and (K - created[i][j]) / maps[i][j] < 2:
                count += 1
    print('#{} {}'.format(tc, count))

# 1
# 2 2 10
# 1 1
# 0 2