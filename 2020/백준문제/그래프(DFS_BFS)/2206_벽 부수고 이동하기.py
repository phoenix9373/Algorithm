from collections import deque
import sys

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def bfs(v):
    q = deque()
    q.append(v)
    x, y, check = v[0], v[1], v[2] # check = 1일 때, 벽 안 뚫음.
    visited[0][y][x] = 1
    visited[1][y][x] = 1

    while q:
        t = q.popleft()
        x, y, check = t[0], t[1], t[2]
        if x == M - 1 and y == N - 1:
            return visited[check][y][x]

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < M and 0 <= ny < N:
                # 1. 길이 0(벽없음)일때는 check=0(아직 벽 안 부심.)을 기준으로 방문 체크.
                if arr[ny][nx] == 0 and visited[check][ny][nx] == 0:
                    q.append([nx, ny, check])
                    visited[check][ny][nx] = visited[check][y][x] + 1
                # 2. 1(벽있음)인데 check=0(아직 벽을 안 부순 경우)인 경우,
                #    벽 한 번 부시고(부신 이후부터 check=1로 변함.)
                #    부신 곳을 그 이전 방문 값(check=0일때 visited값) + 1을 한다.
                elif arr[ny][nx] == 1 and check == 0:
                    q.append([nx, ny, 1])
                    visited[1][ny][nx] = visited[check][y][x] + 1
    return -1


N, M = map(int, sys.stdin.readline().split())
arr = [list(map(int, ' '.join(sys.stdin.readline()).split())) for _ in range(N)]

visited = [[[0] * M for _ in range(N)] for _ in range(2)]
res = bfs([0, 0, 0]) # 벽을 부순 순간 1로 바뀐다고 가정.
print(res)
for k in visited:
    for i in k:
        print('/'.join(map(str, i)))
    print()
'''
5 10
0000011000
1101011010
0000000010
1111111110
1111000000'''