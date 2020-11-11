for tc in range(1, int(input()) + 1):
    n, m = map(int, input().split())
    q = list(map(int, input().split()))
    m = m % n
    print('#{} {}'.format(tc, q[m]))