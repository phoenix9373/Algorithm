di = [1, -1, 0, 0]
dj = [0, 0, 1, -1]

def bfs(v):
    q = []
    q.append(v)
    visited[v[0]][v[1]] = 1

    while q:
        t = q.pop(0)
        i, j = t[0], t[1]

        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < n and 0 <= nj < n and visited[ni][nj] == 0 and arr[ni][nj] != 1:
                if arr[ni][nj] == 0:
                    q.append([ni, nj])
                    visited[ni][nj] = visited[i][j] + 1
                if arr[ni][nj] == 3:
                    return visited[i][j] - 1
    return 0


def find_start():
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 2:
                return [i, j]


for tc in range(1, int(input()) + 1):
    n = int(input())
    arr = [list(map(int, list(input()))) for _ in range(n)]
    visited = [[0] * n for _ in range(n)]
    s = find_start()
    result = bfs(s)
    print('#{} {}'.format(tc, result))
