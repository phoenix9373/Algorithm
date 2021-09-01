import sys
from collections import deque

sys.stdin = open('input.txt', 'r')

dx = [2, 2, -2, -2, 1, 1, -1, -1]
dy = [1, -1, 1, -1, 2, -2, 2, -2]


def bfs(s):
    check = False
    x, y = s[0], s[1]

    q = deque()
    q.append([x, y])

    while q:
        x, y = q.popleft()

        if maps[x][y] == 1:
            check = visited[x][y]
            break

        for k in range(8):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                q.append([nx, ny])
                visited[nx][ny] = visited[x][y] + 1

    return check


for tc in range(1, int(input()) + 1):
    N = int(input())
    maps = [[0] * N for _ in range(N)]
    sx, sy = map(int, input().split())
    ex, ey = map(int, input().split())
    maps[ex][ey] = 1
    visited = [[0] * N for _ in range(N)]

    # 8개의 방향을 주고,
    # BFS로 탐색하면서,
    # check 가 true가 되면,
    # 모두 멈추고,
    # 해당 움직인 거리를 출력한다.
    # visit check를 하자...!

    ans = bfs([sx, sy])
    print(ans)