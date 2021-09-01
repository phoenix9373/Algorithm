di = [1, -1, 0, 0]
dj = [0, 0, 1, -1]


def sol(i, j, c, s):
    global maxH
    if maxH < s + 1:
        maxH = s + 1

    visited[i][j] = 1

    for k in range(4):
        ni = i + di[k]
        nj = j + dj[k]

        if 0 <= ni < N and 0 <= nj < N:
            


for tc in range(1, int(input()) + 1):
    N, K = map(int, input().split())
    maps = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    maxH = 0