import sys

sys.stdin = open('input.txt', 'r')
from collections import deque

di = [1, -1, 0, 0]
dj = [0, 0, 1, -1]


def sol():
    most_home_count = 0

    # 모든 좌표에 대해 수행.
    cnt = 0
    for r in range(N):
        for c in range(N):

            # k값 마다 시행.
            k = 0
            while k < MAX_K:
                # 각 k 값에 대한 시도마다 q, visited 초기화.
                q = deque()
                q.append((r, c))
                visited = [[0] * N for _ in range(N)]
                visited[r][c] = 1

                k += 1
                home = 0
                cost = k ** 2 + (k - 1) ** 2
                while q:
                    i, j = q.popleft()

                    if maps[i][j] == 1:
                        home += 1

                    if visited[i][j] == k:
                        continue

                    for x in range(4):
                        ni = i + di[x]
                        nj = j + dj[x]
                        if 0 <= ni < N and 0 <= nj < N and not visited[ni][nj]:
                            if visited[i][j] < k:
                                visited[ni][nj] = visited[i][j] + 1
                                q.append((ni, nj))
                if home * M - cost >= 0 and home > most_home_count:
                    most_home_count = home

    return most_home_count


for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    maps = [list(map(int, input().split())) for _ in range(N)]
    MAX_K = 0
    home_cnt = 0
    for i in range(N):
        for j in range(N):
            if maps[i][j] == 1:
                home_cnt += 1
    while MAX_K ** 2 + (MAX_K - 1) ** 2 <= home_cnt * M:
        MAX_K += 1
    MAX_K -= 1
    ans = sol()
    print('#{} {}'.format(tc, ans))
