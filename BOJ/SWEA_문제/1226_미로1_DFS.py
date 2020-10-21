dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def dfs(v):
    global result

    i, j = v[0], v[1]
    visited[i][j] = 1

    for k in range(4):
        ni = i + dx[k]
        nj = j + dy[k]

        if 0 <= ni < n and 0 <= nj < n and visited[ni][nj] == 0:
            if arr[ni][nj] == 0:
                dfs([ni, nj])

            if arr[ni][nj] == 3:
                result = 1


for _ in range(1, 11):
    tc = int(input())
    n = 16
    arr = [list(map(int, list(input()))) for _ in range(n)]
    visited = [[0] * n for _ in range(n)]
    s = 0 # 시작점.
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 2:
                s = [i, j]
                break
        if s != 0:
            break
    result = 0
    dfs(s)
    print('#{} {}'.format(tc, result))