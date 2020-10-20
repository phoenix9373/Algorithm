def choice(idx, cumsum=0):
    global min_value

    if idx == N: # N번째 값까지 조회하고 스탑.
        if cumsum - B < min_value and cumsum >= B:
            min_value = cumsum - B
        return

    if cumsum - B > min_value: # 가지치기. 나는 cumsum과 B만 보고 있어서 가지치기를 안 했음. min_value도 추가했어야함.
        return

    choice(idx + 1, cumsum + arr[idx])
    choice(idx + 1, cumsum)



for tc in range(1, int(input()) + 1):
    N, B = map(int, input().split())
    arr = list(map(int, input().split()))
    min_value = pow(2, 30)
    choice(0)
    print('#{} {}'.format(tc, min_value))