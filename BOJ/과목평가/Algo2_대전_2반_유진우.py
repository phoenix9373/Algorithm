di = [1, -1, 0, 0]
dj = [0, 0, 1, -1]


def get_count(x, y, K):
    # x, y는 각각 시작점의 index.
    # K = arr[x][y]
    # 시작점에서 상하좌우 조회, 범위 제한, 그리고 값이 1이상이면 방문체크.

    visited[x][y] = 1  # 시작점은 반드시 1이상이므로 방문체크.

    x_tmp, y_tmp = x, y  # x, y는 항상 원점으로 유지하기 위해 임시 좌표값 설정.
    for t in range(4):  # 4개 방향을 탐색.
        for _ in range(K):  # 총 K번만큼 한 방향으로 이동하면서 탐색.
            nx = x_tmp + di[t]
            ny = y_tmp + dj[t]
            # 범위 제한 조건, 방문 체크 유무, 폭탄 유무에 따라 방문 체크.
            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == 0 and arr[nx][ny] > 0:
                visited[nx][ny] = 1  # 조건을 만족한 위치는 방문 체크.
                get_count(nx, ny, arr[nx][ny])  # 조건을 만족한 위치에서 다시 탐색한다.
            x_tmp, y_tmp = nx, ny  # 한 방향으로 이동할 때는 이동한 점으로 기준점 이동.
        x_tmp, y_tmp = x, y  # 한 방향으로 이동이 끝나면 다시 원점으로 기준점 이동.


for tc in range(1, int(input()) + 1):
    N = int(input())
    R, C = map(int, input().split())  # 시작점.
    arr = [list(map(int, input().split())) for _ in range(N)]  # 폭탄 배열.
    visited = [[0] * N for _ in range(N)]  # 방문 체크 배열.
    get_count(R, C, arr[R][C])  # 시작점에서 폭발 시작.

    rep = sum([sum(row) for row in visited])  # 각 row마다 sum을 구해서 리스트를 만들고, 최종으로 sum을 구함.

    print('#{} {}'.format(tc, rep))
