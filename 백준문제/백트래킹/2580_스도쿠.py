# 2020.11.04 미완

import sys

sys.stdin = open('input.txt', 'r')

maps = [list(map(int, input().split())) for _ in range(9)]

starts = [[i, j] for i in range(9) for j in range(9) if maps[i][j] == 0]
visited = [0] * len(starts)


def sol(cnt):
    if cnt == len(starts):
        for x in range(9):
            print(*maps[x])
        return

    v = starts[cnt]
    i, j = v[0], v[1]
    ni, nj = (i // 3) * 3, (j // 3) * 3

    tmp = [maps[di][dj] for di in range(ni, ni + 3) for dj in range(nj, nj + 3) if maps[di][dj] != 0]
    cands = [k for k in range(1, 10) if k not in maps[i] and k not in list(zip(*maps))[j] and k not in tmp]

    if not cands:
        return

    for w in cands:
        maps[i][j] = w
        sol(cnt + 1)


sol(0)
# print(*maps, sep='\n')