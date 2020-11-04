from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def bfs(v): # v = [x, y, used] / used는 처음에 0으로 시작.
    q = deque()
    q.append(v)

    x, y, used = v[0], v[1], 0
    visited[used][y][x] = 1

    while q:
        t = q.popleft()
        x, y, used = t[0], t[1], t[2] # q에 있는 요소의 좌표와 used를 새로 받음.

        if x == Ex and y == Ey:
            return visited[used][y][x] - 1

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < M and 0 <= ny < N:
                if arr[ny][nx] == 0 and visited[used][ny][nx] == 0:
                    q.append([nx, ny, used])
                    visited[used][ny][nx] = visited[used][y][x] + 1
                elif arr[ny][nx] == 1 and used == 0:
                    q.append([nx, ny, 1]) # 사용완료했다는 표시 전달.
                    visited[1][ny][nx] = visited[0][y][x] + 1
    return -1

N, M = map(int, input().split()) # 5 6 / y x
Hy, Hx = map(lambda x: int(x) - 1, input().split()) # 0 0
Ey, Ex = map(lambda x: int(x) - 1, input().split()) # 4 5 / y x

arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[[0] * M for _ in range(N)] for _ in range(2)]
res = bfs([Hx, Hy, 0])
print(res)