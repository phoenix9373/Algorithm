dx = [-1, 1, 0]
dy = [0, 0, -1]

def dfs(v):
    global result
    i, j = v[0], v[1]
    visited[i][j] = 1
    if i == 0:
        result = j

    for k in range(3):
        ni = i + dy[k]
        nj = j + dx[k]
        if 0 <= ni < 100 and 0 <= nj < 100 and visited[ni][nj] == 0 and arr[ni][nj] == 1:
            dfs([ni, nj])
            break

for tc in range(1, 11):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    visited = [[0] * 100 for _ in range(100)]
    result = 0
    s = [99, arr[99].index(2)]
    dfs(s)

    print('#{} {}'.format(tc, result))