for tc in range(1, int(input())+1):
    n, k = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    arr_T = list(zip(*arr))
    result = 0
    for em in [arr, arr_T]:
        for i in range(n):
            cnt = 0
            for j in range(n-1):
                if em[i][j] == 1:
                    cnt += 1
                    if cnt == k and em[i][j+1] == 0:
                        result += 1
                    elif cnt == k-1 and j == n-2 and em[i][n-1] == 1:
                        result += 1
                else:
                    cnt = 0

    print('#{} {}'.format(tc, result))