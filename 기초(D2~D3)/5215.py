for c in range(1, int(input())+1):
    n, l = map(int, input().split())
    tk = [list(map(int, input().split())) for _ in range(n)]
    M = 0
    for i in range(1<<n):
        t_sum, k_sum = 0, 0
        for j in range(n):
            if (i & (1<<j)) and k_sum <= l:
                t_sum += tk[j][0]
                k_sum += tk[j][1]
        if k_sum <= l and t_sum > M:
            M = t_sum
    print(f'#{c} {M}')