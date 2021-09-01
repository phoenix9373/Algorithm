for tc in range(1, int(input()) + 1):

    n, m = map(int, input().split())
    MIN = n*m
    char_list = [list(input()) for _ in range(n)]

    cases = [(i, j, k) for i in range(n-2) for j in range(i+1, n-1) for k in range(j+1, n)]
    for i, j, k in cases:
        value = 0
        for r in range(n):
            for c in range(m):
                if r <= i and char_list[r][c] != 'W':
                    value += 1
                if i < r and r <= j and char_list[r][c] != 'B':
                    value += 1
                if r > j and char_list[r][c] != 'R':
                    value += 1
        if MIN > value:
            MIN = value
    print('#{} {}'.format(tc, MIN))


# --이병훈 풀이--
for t in range(int(input())):

    N, M = map(int, input().split())
    W = [0] * N
    B = [0] * N
    R = [0] * N
    flag = [input() for _ in range(N)]
    # i의 범위는 0부터 N-3
    # j의 범위는 i+1부터 N-2
    # k의 범위는 j+1부터 N-1
    for idx, line in enumerate(flag):
        for element in line:
            if element != 'W':
                W[idx] += 1
            if element != 'B':
                B[idx] += 1
            if element != 'R':
                R[idx] += 1
        if idx != 0:
            W[idx] += W[idx - 1]
            B[idx] += B[idx - 1]
            R[idx] += R[idx - 1]
    MIN = N * M
    for i in range(N - 2):
        for j in range(i + 1, N - 1):
            SUM = W[i] + B[j] - B[i] + R[N - 1] - R[j]
            if MIN > SUM:
                MIN = SUM
    print('#{} {}'.format(t + 1, MIN))