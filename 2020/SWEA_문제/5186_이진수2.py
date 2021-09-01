for tc in range(1, int(input()) + 1):
    n = float(input())
    res = ''
    while n != 0:
        n *= 2
        if n >= 1:
            n -= 1
            res += '1'
        else:
            res += '0'

        if len(res) > 12:
            res = 'overflow'
            break

    print('#{} {}'.format(tc, res))