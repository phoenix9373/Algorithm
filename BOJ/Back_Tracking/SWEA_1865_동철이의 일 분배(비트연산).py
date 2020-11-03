def DFS(flag, idx, value):
    global ans
    if flag == (1 << N) - 1:
        if ans < value * 100:
            ans = value * 100
        return
        # 진행할 수록 값이 작아지니 이미 구한 값보다 작다면 필요없다.
    if value * 100 <= ans:
        return

    for i in range(N):
        # 해당 일은 이미 배정되어서 처리함.
        if flag & (1 << i): continue
        DFS(flag | 1 << i, idx + 1, value * (work[idx][i] / 100))


for tc in range(1, int(input()) + 1):
    N = int(input())

    work = [list(map(int, input().split())) for _ in range(N)]

    ans = 0
    #flag, idx, value

    DFS(0, 0, 1)

    print("#{} {:.6f}".format(tc, ans))