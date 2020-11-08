from collections import deque
import heapq

di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]


def djikstra():
    D = [[float('inf')] * N for _ in range(N)]
    D[0][0] = 0

    q = deque()
    q.append((0, 0))

    while q:
        i, j = q.popleft()

        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < N and 0 <= nj < N:
                # 갱신
                if arr[ni][nj] > arr[i][j]:
                    tmp = 1 + arr[ni][nj] - arr[i][j]
                else:
                    tmp = 1

                if D[ni][nj] > D[i][j] + tmp:
                    D[ni][nj] = D[i][j] + tmp
                    q.append((ni, nj))
    return D[N - 1][N - 1]


for tc in range(1, int(input()) + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = djikstra()
    print('#{} {}'.format(tc, ans))