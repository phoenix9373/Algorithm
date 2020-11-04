def sol(v, cum):
    global ans

    if cum > ans:
        return

    if v == N:
        if cum < ans:
            ans = cum
        return

    for i in range(N):
        if visited[i] == 0:
            visited[i] = 1
            sol(v + 1, cum + info[v][i])
            visited[i] = 0


for tc in range(1, int(input()) + 1):
    N = int(input())
    info = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N
    ans = pow(2, 30)
    sol(0, 0)
    print('#{} {}'.format(tc, ans))