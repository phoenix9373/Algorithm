# 미로1과 달리 100 * 100 이기때문에 BFS로 풀이.
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(v):
    i, j = v[0], v[1]
    q = []
    visited[i][j] = 1
    q.append([i, j])

    while q:
        t = q.pop(0)
        i, j = t[0], t[1]

        for k in range(4):
            ni = i + dx[k]
            nj = j + dy[k]
            if visited[ni][nj] == 0:
                if arr[ni][nj] == 3:
                    return 1
                if arr[ni][nj] == 0:
                    q.append([ni, nj])
                    visited[ni][nj] = visited[i][j] + 1
    return 0


for _ in range(1, 11):
    tc = int(input())
    n = 100
    arr = [list(map(int, list(input()))) for _ in range(n)]
    visited = [[0] * n for _ in range(n)]
    s = 0
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 2:
                s = [i, j]
                break
        if s:
            break
    result = bfs(s)
    print('#{} {}'.format(tc, result))