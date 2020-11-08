arr = [list(map(int,input().split())) for _ in range(9)]
holes = []
holes = [(i, j) for i in range(9) for j in range(9) if arr[i][j] == 0]


def check(x, y):
    tmp = [i for i in range(1, 10)]
    for j in range(9):
        if arr[x][j] in tmp:
            tmp.remove(arr[x][j])
        if arr[j][y] in tmp:
            tmp.remove(arr[j][y])

    nx = (x // 3) * 3
    ny = (y // 3) * 3

    for i in range(nx, nx + 3):
        for j in range(ny, ny + 3):
            if arr[i][j] in tmp:
                tmp.remove(arr[i][j])
    return tmp


flag = False
def sol(idx):
    global flag

    if flag:
        return

    if idx == len(holes):
        for row in arr:
            print(*row)
        flag = True
        return

    x, y = holes[idx]
    temp = check(x, y)

    for w in temp:
        arr[x][y] = w
        sol(idx + 1)
        arr[x][y] = 0

sol(0)