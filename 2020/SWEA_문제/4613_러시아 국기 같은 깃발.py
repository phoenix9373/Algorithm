for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]

    ans = 99999999
    for i in range(N - 2):
        for j in range(i + 1, N - 1):
            cnt = 0
            for x in range(N):
                if x <= i:
                    cnt += M - arr[x].count('W')
                elif i < x <= j:
                    cnt += M - arr[x].count('B')
                elif x > j:
                    cnt += M - arr[x].count('R')
            if cnt < ans:
                ans = cnt


    print('#{} {}'.format(tc, ans))