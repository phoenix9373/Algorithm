def perm(row, idx, cum_sum):
    global min_sum

    if row == n:
        if sum(sel) < min_sum:
            min_sum = sum(sel)
        return

    if cum_sum >= min_sum: # 가지치기.
        return

    for i in range(n):
        if col_check[i] == 0:
            sel[idx] = arr[row][i]

            col_check[i] = 1
            perm(row + 1, idx + 1, cum_sum + arr[row][i])
            col_check[i] = 0


for tc in range(1, int(input()) + 1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    # visited = [[0] * n for _ in range(n)]
    col_check = [0] * n
    sel = [0] * n
    min_sum = pow(2, 20)
    perm(0, 0, 0)

    print('#{} {}'.format(tc, min_sum))