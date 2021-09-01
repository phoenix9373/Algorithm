di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

# 가로(j) C, 세로(i) R
C, R = map(int, input().split())
K = int(input())

arr = [[0] * C for _ in range(R)]
seat_num = [[(j + 1, 6 - i) for j in range(C)] for i in range(R)]

# 시작점 = (R - 1, 0)
arr[R - 1][0] = 1
i, j = R - 1, 0
while True:
    for k in range(4):
        while True:
            i += di[k]
            j += dj[k]
            if 0 <= i < R and 0 <= j < C and arr[i][j] == 0:
                arr[i][j] = arr[i - di[k]][j - dj[k]] + 1
            else:
                i -= di[k]
                j -= dj[k]
                break
    if i == R//2 and j == C//2:
        break


def answer(k, arrs, seats):
    for r, row in enumerate(arrs):
        if k in row:
            return seats[r][row.index(k)]
    return [0]


res = answer(K, arr, seat_num)
print(*res)