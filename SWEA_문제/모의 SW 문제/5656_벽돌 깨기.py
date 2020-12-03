from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def sol(pos_list, arr, c):
    global minV

    if c == N:
        bricks = 0
        for i in range(H):
            for j in range(W):
                if arr[i][j] != 0:
                    bricks += 1
        if bricks < minV:
            minV = bricks
        return

    # dfs
    for j in pos_list:
        th = 0
        for i in range(H):
            if arr[i][j] != 0:
                th = i
                break
        # bfs
        q = deque()
        q.append([th, j])
        axis_list = [[th, j]]
        visited = [[0] * W for _ in range(H)]
        visited[th][j] = 1

        while q:
            x, y = q.popleft()
            R = arr[x][y] - 1

            for k in range(4):
                for r in range(1, R + 1):
                    nx, ny = x + dx[k] * r, y + dy[k] * r
                    if 0 <= nx < H and 0 <= ny < W and arr[nx][ny] != 0:
                        if visited[nx][ny] == 0:
                            visited[nx][ny] = 1
                            axis_list.append([nx, ny])
                            q.append([nx, ny])
        del visited

        new_arr = [[0] * W for _ in range(H)]

        for w in range(W):
            p = H - 1
            for h in range(H - 1, -1, -1):
                while [p, w] in axis_list:
                    p -= 1
                if p == -1 or arr[p][w] == 0:
                    break
                new_arr[h][w] = arr[p][w]
                p -= 1

        # if tmp == [2, 2, 6]:
        #     print(*new_arr, sep='\n')

        sub_pos_list = [i for i in range(W) if new_arr[H - 1][i] != 0]
        sol(sub_pos_list, new_arr, c + 1)

        del new_arr


for tc in range(1, int(input()) + 1):
    N, W, H = map(int, input().split())
    maps = [list(map(int, input().split())) for _ in range(H)]
    minV = float('inf')
    possible = [i for i in range(W) if maps[H - 1][i] != 0]  # 맨 밑이 0이 아닌 경우.

    sol(possible, maps, 0)
    if minV == float('inf'):
        minV = 0
    print('#{} {}'.format(tc, minV))

# 1
# 3 10 10
# 0 0 0 0 0 0 0 0 0 0
# 1 0 1 0 1 0 0 0 0 0
# 1 0 3 0 1 1 0 0 0 1
# 1 1 1 0 1 2 0 0 0 9
# 1 1 4 0 1 1 0 0 1 1
# 1 1 4 1 1 1 2 1 1 1
# 1 1 5 1 1 1 1 2 1 1
# 1 1 6 1 1 1 1 1 2 1
# 1 1 1 1 1 1 1 1 1 5
# 1 1 7 1 1 1 1 1 1 1
