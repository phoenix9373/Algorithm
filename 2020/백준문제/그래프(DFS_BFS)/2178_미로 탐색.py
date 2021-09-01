from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def BFS(v):

    q = deque()
    q.append(v)
    x, y = v[0], v[1]
    visited[y][x] = 1

    while q:
        t = q.popleft()
        x, y = t[0], t[1]

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < M and 0 <= ny < N and visited[ny][nx] == 0 and arr[ny][nx] == 1:
                q.append([nx, ny])
                visited[ny][nx] = visited[y][x] + 1


N, M = map(int, input().split())

arr = [list(map(int, ' '.join(input()).split())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]

BFS([0, 0])
print(visited[N-1][M-1])