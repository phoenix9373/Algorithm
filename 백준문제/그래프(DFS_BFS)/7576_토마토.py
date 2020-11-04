from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


# v 값에 들어가는 것은 시작점. but 시작점을 여러개로 해서
# q에 각각의 시작점을 진행하면 동시에 시작하는 효과가 일어난다.
def bfs(v):
    # 시작부터 모두 익어있으면 0 반환.
    check = [row.count(0) for row in arr]
    if sum(check) == 0:
        return 0

    q = deque()
    for s in v:
        q.append(s) # 처음의 시작점을 모두 q에 넣어준다.
        visited[s[0]][s[1]] = 1
    while q:
        for i in range(len(q)): # 각 시작점에서 출발해서 하루동안 주변부에서 익는 토마토 위치를 모두 q에 넣어준다.
            t = q.popleft()     # 한 턴에 갈 수 있는 모든 곳을 q에 넣으므로, 동시에 진행하게 된다.
            y, x = t[0], t[1]

            for k in range(4):
                nx = x + dx[k]
                ny = y + dy[k]
                if 0 <= nx < M and 0 <= ny < N and arr[ny][nx] == 0 and visited[ny][nx] == 0:
                    q.append([ny, nx])
                    visited[ny][nx] = visited[y][x] + 1

    # bfs를 모두 끝낸 후, 0이 있는지 확인.
    # 하면서 최댓값 갱신
    res = 0
    for i in range(N):
        for j in range(M):
            if visited[i][j] == 0:
                return -1
            if visited[i][j] > res:
                res = visited[i][j]

    # 0이 없으면 bfs 결과 중 최대값 출력
    return res - 1


M, N = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
starts = []
for n in range(N):
    for m in range(M):
        if arr[n][m] == 1:
            starts.append([n, m])
        if arr[n][m] == -1:
            visited[n][m] = -1

result = bfs(starts)
print(result)