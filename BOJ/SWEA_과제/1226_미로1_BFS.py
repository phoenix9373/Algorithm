# bfs(s, N)            # s 시작노드, N 마지막노드
    # 큐 생성
    # 시작점 enQ()
    # visited 생성
    # 시작점 방문 표시
    # while 큐가 비어있지 않으면:
        # t = deQ()
        # t 노드는 시작점에 인접한 노드
        # t 노드에 대한 처리(enQ, 방문 등)??? 아래 과정에서 함. 시작점일 경우 함수 호출 바로 밑에서.
        # t에 인접한 모든 노드 i가 처리 전이면
            # for
            # i를 enQ()
            # i를 방문 처리.
            # tip) visited[i] = visited[t] + 1로 하면 최단거리를 구할 수 있다.
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
def bfs(v):
    i, j = v[0], v[1]

    Q = []
    visited[i][j] = 1
    Q.append(v)

    while Q:
        t = Q.pop(0)
        x, y = t[0], t[1]

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0:
                if arr[nx][ny] == 0:
                    Q.append([nx, ny])
                    visited[nx][ny] = visited[x][y] + 1  # 최단거리 구하는데 유용함.
                elif arr[nx][ny] == 3:
                    return 1
    return 0


for _ in range(1, 11):
    tc = int(input())
    n = 16
    arr = [list(map(int, list(input()))) for _ in range(n)]
    visited = [[0] * n for _ in range(n)]
    s = 0
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 2:
                s = [i, j]
                break
        if s != 0:
            break

    result = bfs(s)
    print('#{} {}'.format(tc, result))