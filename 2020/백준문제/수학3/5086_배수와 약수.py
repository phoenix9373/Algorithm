while True:
    a, b = map(int, input().split())

    if a == b == 0:
        break

    ans = ''

    if (a // b) * b == a:
        ans = 'multiple'
    elif (b // a) * a == b:
        ans = 'factor'
    else:
        ans = 'neither'

    print(ans)