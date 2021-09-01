# 1010, 212
# 1110, 112
b = [['1'], ['0']]
t = [['1', '2'], ['0', '2'], ['0', '1']]

for tc in range(1, int(input()) + 1):
    bi = input()
    tr = input()

    def solution(n, num, ref):
        ret = []
        for i in range(len(num)):
            tmp = [x for x in num]
            for j in range(n):
                for k in ref[j]:
                    tmp[i] = k
                    ret.append(int(''.join(tmp), n))

        return ret
    bi = solution(2, bi, b)
    tr = solution(3, tr, t)

    res = list(set(bi) & set(tr))[0]
    print('#{} {}'.format(tc, res))