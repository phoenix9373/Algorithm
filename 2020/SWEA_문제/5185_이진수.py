def Bbit_print(i):
    ret = ''
    for j in range(3, -1, -1):
        ret += '1' if i & (1 << j) else '0'
    print(ret, end='')


for tc in range(1, int(input()) + 1):
    N, num = input().split()

    print('#{}'.format(tc), end=' ')

    for i in range(int(N)):
        tmp = int(num[i], 16)
        Bbit_print(tmp)

    print()