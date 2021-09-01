def sol(s, cnt):
    global ans

    if cnt >= ans:
        return

    if s == N:
        if cnt < ans:
            ans = cnt
        return

    for i in range(1, info[s] + 1):
        sol(s + i, cnt + 1)


for tc in range(1, int(input()) + 1):
    info = list(map(int, input().split()))
    N, info = info[0], [0] + info[1:]
    state = [0] * (N + 1)
    ans = pow(2, 30)
    sol(1, 0)
    print('#{} {}'.format(tc, ans - 1))