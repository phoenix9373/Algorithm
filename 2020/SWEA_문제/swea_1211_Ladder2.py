dx = [-1, 1, 0]
dy = [0, 0, 1]

def dfs(v):
    global cnt, result
    i, j = v[0], v[1]
    visited[i][j] = 1
    if i == 99:
        result = cnt

    for k in range(3):
        ni = i + dy[k]
        nj = j + dx[k]
        if 0 <= ni < 100 and 0 <= nj < 100 and visited[ni][nj] == 0 and arr[ni][nj] == 1:
            cnt += 1
            dfs([ni, nj])
            break

for tc in range(1, 11):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    s = [[0, idx] for idx, j in enumerate(arr[0]) if j == 1]
    sorting = []
    for x in s:
        visited = [[0] * 100 for _ in range(100)]
        cnt = 0
        result = 0
        dfs(x)
        sorting.append([result, x[1]])
    sorting = sorted(sorting, key=lambda x: (x[0], -x[1]))
    print('#{} {}'.format(tc, sorting[0][1]))