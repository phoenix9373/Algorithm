from collections import deque

T = int(input())

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def BFS(v):
    global ans
    ans += 1

    x, y = v[0], v[1]
    q = deque()
    q.append(v)

    visited[y][x] = 1

    while q:
        tmp = q.popleft()
        x, y = tmp[0], tmp[1]

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if -1 < nx < M and -1 < ny < N and visited[ny][nx] == 0 and arr[ny][nx] == 1:
                q.append([nx, ny])
                visited[ny][nx] = 1


for tc in range(1, T + 1):
    # 가로, 세로, 배추 위치
    M, N, K = map(int, input().split())
    arr = [[0] * M for _ in range(N)]
    visited = [[0] * M for _ in range(N)]
    ans = 0

    # 배추 위치 입력.
    for _ in range(K):
        x, y = map(int, input().split())
        arr[y][x] = 1

    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1 and visited[i][j] == 0:
                BFS([j, i])

    print(ans)