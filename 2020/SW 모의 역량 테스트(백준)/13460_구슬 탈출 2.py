from collections import deque

N, M = map(int, input().split())
maps = [' '.join(input()).split() for _ in range(N)]
visited = [[[0, 0]] * M for _ in range(N)]
r, b, o = (0, 0, 0)
for i in range(N):
    for j in range(M):
        if maps[i][j] == 'R':
            r = (i, j)
        if maps[i][j] == 'B':
            b = (i, j)
        if maps[i][j] == 'O':
            o = (i, j)

di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]


def sol(r, b, o):
    oi, oj = o[0], o[1]
    q = deque()
    q.append([r[0], r[1], b[0], b[1], 0])
    visited[r[0]][r[1]][0] = 1
    visited[b[0]][b[1]][0] = 1

    while q:
        ri, rj, bi, bj, cnt = q.popleft()

        for k in range(4):
            ni, nj = ri, rj
            mi, mj = bi, bj
            while maps[ni][nj] != '#':
                if (ni, nj) == (oi, oj):
                    pass
                if maps[ni][nj] == '.':
                    ni += di[k]
                    nj += dj[k]
                if maps[ni][nj] == 'B':
                    while maps[mi][mj] != '#':
                        mi += di[k]
                        mj += dj[k]
            while maps[mi][mj] != '#':
                if (mi, mj) == (oi, oj):
                    pass
                if maps[mi][mj] == '.':
                    mi += di[k]
                    mj += dj[k]
                if maps[mi][mj] == 'B':
                    while maps[ni][nj] != '#':
                        ni += di[k]
                        nj += dj[k]