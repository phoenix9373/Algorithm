# 56개의 숫자를 받아서, 7개씩 판단.
# 총 8개의 숫자 반환.
# 0001101, 0011001, 0010011, 0111101, 0100011, 0110001, 0101111, 0111011, 0110111, 0001011
def check(x):
    res = [0] * 8
    code = ['0001101', '0011001', '0010011', '0111101', '0100011', '0110001', '0101111', '0111011', '0110111',
            '0001011']
    k = 0
    for i in range(8):
        tmp = x[i * 7:(i + 1) * 7]
        res[i] = code.index(tmp)
        if i % 2 == 1:
            k += res[i]
        else:
            k += res[i] * 3

    if k % 10 == 0:
        return sum(res)
    else:
        return 0


for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    # arr = [input()[::-1] for _ in range(N)]
    codes = ''
    for i in range(N):
        line = input()[::-1]
        if '1' in line:
            t = line.index('1')
            codes = line[t:t + 56]

    result = check(codes[::-1])
    print('#{} {}'.format(tc, result))