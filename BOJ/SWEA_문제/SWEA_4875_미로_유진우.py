dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def miro(v):  # 시작점.
    stack.append(v)

    while len(stack) > 0:
        pos = stack.pop()
        i, j = pos[0], pos[1]
        visited[i][j] = 1

        for k in range(4):
            ni = i + dx[k]
            nj = j + dy[k]
            if 0 <= ni < n and 0 <= nj < n and visited[ni][nj] == 0:
                if arr[ni][nj] == 0:
                    stack.append([ni, nj])

                if arr[ni][nj] == 3:
                    return 1
    return 0


for tc in range(1, int(input())+1):
    n = int(input())
    arr = [list(map(int, list(input()))) for _ in range(n)]
    visited = [[0] * n for _ in range(n)]
    stack = []
    start = 0
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 2:
                start = [i, j]
    if start:
        result = miro(start)
    else:
        result = 0
    print('#{} {}'.format(tc, result))
