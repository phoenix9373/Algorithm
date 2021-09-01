N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
cnt_0 = 0
cnt_1 = 0


def sol(x, y, n):
    if n == 1:

        return arr[x][y]

    r1 = sol(x, y, n // 2)
    r2 = sol(x + n // 2, y, n // 2)
    r3 = sol(x, y + n // 2, n // 2)
    r4 = sol(x + n // 2, y + n // 2, n // 2)

    if r1 == r2 == r3 == r4:
        return r1
    else:
        global cnt_0, cnt_1
        for i in [r1, r2, r3, r4]:
            if i != None:
                if i:
                    cnt_1 += 1
                else:
                    cnt_0 += 1


sol(0, 0, N)
print(cnt_0)
print(cnt_1)
