import sys

sys.stdin = open('input.txt', 'r')

di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]


def Dijkstra(G):
    D = [[float('inf')] * N for _ in range(N)] # key
    visited = [[False] * N for _ in range(N)] # visited
    D[0][0] = 0

    check = set() # 탐색 하는 경로
    check.add((0, 0))

    while True:
        mi, mj = -1, -1
        min_val = float('inf')

        for i, j in check:
            if not visited[i][j] and D[i][j] < min_val:
                min_val = D[i][j]
                mi, mj = i, j

        visited[mi][mj] = 1
        check.remove((mi, mj))

        if mi == mj == N - 1:
            return D[mi][mj]

        for k in range(4):
            ni = mi + di[k]
            nj = mj + dj[k]
            if 0 <= ni < N and 0 <= nj < N and not visited[ni][nj]:
                tmp = G[ni][nj] - G[mi][mj] + D[mi][mj] + 1 if G[ni][nj] > G[mi][mj] else D[mi][mj] + 1
                if tmp < D[ni][nj]:
                    D[ni][nj] = tmp
                    check.add((ni, nj))


for tc in range(1, int(input()) + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = Dijkstra(arr)
    print('#{} {}'.format(tc, ans))
