# 델타 이동 + 재귀함수 DFS
# DFS에는 stack과 재귀로 구현하는 방법이 있다.
# 벽 = 1, 시작점 = 2, 도착점 = 3
# 벽이 있다는 조건이 없으면 범위 조건을 설정해야한다. but 가상의 벽을 만들면 범위 조건을 설정할 필요가 없어진다.
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def dfs(v): # v = [i, j]
    global result
    i, j = v[0], v[1]
    visited[i][j] = 1

    for k in range(4):
        ni = i + dy[k]
        nj = j + dx[k]
        if 0 <= ni < 16 and 0 <= nj < 16 and visited[ni][nj] == 0 and arr[ni][nj] != 1:
            if arr[ni][nj] == 3:
                result = 1
            else:
                tmp = [ni, nj]
                dfs(tmp)


for _ in range(1, 11):
    tc = int(input())
    # 도달 가능 여부: 1(도달), 0(불가)
    arr = [list(map(int, input())) for _ in range(16)]
    # 시작점을 설정한다.
    for x in range(16):
        for y in range(16):
            if arr[x][y] == 2:
                s = [x, y]
    visited = [[0] * 16 for _ in range(16)]
    result = 0
    dfs(s)
    print('#{} {}'.format(tc, result))