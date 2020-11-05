import sys
from collections import deque

sys.stdin = open('input.txt', 'r')

di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]


def Dijkstra(G):
    key = [[float('inf')] * N for _ in range(N)]
    key[0][0] = 0

    q = deque()
    q.append((0, 0))  # 시작점.
    while q:
        i, j = q.popleft()

        # if i == j == N - 1:
        #     return key[i][j]

        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < N and 0 <= nj < N:
                if arr[ni][nj] > arr[i][j]:
                    tmp = arr[ni][nj] - arr[i][j] + 1
                else:
                    tmp = 1
                if key[ni][nj] > key[i][j] + tmp:
                    key[ni][nj] = key[i][j] + tmp
                    q.append((ni, nj))
    return key


for tc in range(1, int(input()) + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = Dijkstra(arr)
    print('#{} {}'.format(tc, ans[N-1][N-1]))
