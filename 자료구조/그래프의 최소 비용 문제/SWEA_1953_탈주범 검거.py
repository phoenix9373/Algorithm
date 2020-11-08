import sys

sys.stdin = open('input.txt', 'r')
from collections import deque

di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]
case = [[], [i for i in range(4)], [0, 1], [2, 3], [0, 3], [1, 3], [1, 2], [0, 2]]
pos = []


def bfs(s):
    global ans

    q = deque()
    q.append(s)
    visited[s[0]][s[1]] = 1

    while q:
        i, j = q.popleft()

        for k in case[maps[i][j]]:
            ni = i + di[k]
            nj = j + dj[k]

            if not (0 <= ni < N and 0 <= nj < M):
                continue

            if k == 0 and 1 not in case[maps[ni][nj]]:
                continue
            elif k == 1 and 0 not in case[maps[ni][nj]]:
                continue
            elif k == 2 and 3 not in case[maps[ni][nj]]:
                continue
            elif k == 3 and 2 not in case[maps[ni][nj]]:
                continue

            if not visited[ni][nj] and maps[ni][nj] != 0:
                if visited[i][j] < L:
                    ans += 1
                    visited[ni][nj] = visited[i][j] + 1
                    q.append((ni, nj))


for tc in range(1, int(input()) + 1):
    N, M, R, C, L = map(int, input().split())  # 가로, 세로, 맨홀 세로, 맨홀 가로, 소요된 시간.
    maps = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0] * M for _ in range(N)]
    ans = 1
    bfs((R, C))
    print('#{} {}'.format(tc, ans))
