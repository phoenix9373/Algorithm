# 메모리 초과.

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def dfs_stack(v):
    i, j = v[0], v[1]
    stack = []

    visited[i][j] = 1
    stack.append([i, j])

    while stack:
        tmp = stack.pop()
        pi, pj = tmp[0], tmp[1]


        for k in range(4):
            ni = pi + dx[k]
            nj = pj + dy[k]

            if 0 <= ni < n and 0 <= nj < n and visited[ni][nj] == 0:
                if arr[ni][nj] == 3:
                    print('done')
                    return 1
                if arr[ni][nj] == 0:
                    visited[ni][nj] = 1
                    stack.append([ni, nj])
    return 0


for _ in range(1, 2):
    tc = int(input())
    n = 16
    arr = [list(map(int, list(input()))) for _ in range(n)]
    visited = [[0] * n for _ in range(n)]

    s = 0
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 2:
                s = [i, j]
                break
        if s != 0:
            break

    result = dfs_stack(s)
    print('#{} {}'.format(tc, result))