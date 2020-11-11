from collections import deque

# 정확히 1 작은 값으로 visited을 늘리면서 탐방.
di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]
def bfs(v):
    cnt = 1
    q = deque()
    q.append(v)

    while q:
        t = q.popleft()
        i, j = t[0], t[1]

        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < N and 0 <= nj < N and arr[i][j] == (arr[ni][nj] + 1):
                q.append([ni, nj])
                cnt += 1
    return cnt, [i,j]


for tc in range(1, int(input()) + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    sort_list = []
    max_val = 0
    for i in range(N):
        for j in range(N):
            tmp, e = bfs([i, j])
            if tmp >= max_val:
                max_val = tmp
                sort_list.append([tmp, arr[e[0]][e[1]]])
    sort_list = sorted(sort_list, key=lambda x: (-x[0], x[1]))
    print('#{} {} {}'.format(tc, sort_list[0][1], sort_list[0][0]))