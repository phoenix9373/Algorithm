# 완전 검색.

import sys
sys.stdin = open('input.txt', 'r')


def solve(v):

    if v == len(delivers):
        global ans
        for i in range(len(homes)):
            tmin = 1e9
            for j in range(len(delivers)):
                if sel[j]:
                    pass

        return

    sel[v] = 1
    solve(v + 1)
    sel[v] = 0
    solve(v + 1)


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    homes = []
    delivers = []

    for i in range(N):
        for j in range(N):
            if arr[i][j] == 1:
                homes.append([i, j])
            elif arr[i][j] > 1:
                delivers.append([i, j, arr[i][j]])

    sel = [0] * len(delivers)
    ans = 0
    distances = [[abs(di - i) + abs(dj - j) for i, j in homes] for di, dj, price in delivers]

    print(distances)