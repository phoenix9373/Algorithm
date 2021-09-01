for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    # 각 행에 색 카운트
    w = [0] * N
    b = [0] * N
    r = [0] * N

    for i in range(N):
        color_arr = input()
        w[i] = color_arr.count('W')
        b[i] = color_arr.count('B')
        r[i] = M - w[i] - b[i] # 나머지이니까.

    # 각 행에서 각각의 컬러를 센 값을 누적. 나중에 행 배분에 따라 누적합으로 사용.
    for i in range(1, N):
        w[i] += w[i - 1]
        b[i] += b[i - 1]
        r[i] += r[i - 1]

    ans = N*M # 이 값 보다는 반드시 작으므로.
    for i in range(N - 2):
        for j in range(i + 1, N - 1):
            # 흰색 칠하기
            cnt = M * (i + 1) - w[i] # 누적했으므로 w[i]를 더하면 된다.
            # 파란색 칠하기
            cnt += M * (j - i) - (b[j] - b[i])
            # 빨간색 칠하기
            cnt += M * (N - 1 - j) - (r[N - 1] - r[j])
            # 합산하기
            if ans > cnt:
                ans = cnt
    print('#{} {}'.format(tc, ans))