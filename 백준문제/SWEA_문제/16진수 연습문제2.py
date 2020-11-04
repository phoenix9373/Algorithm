a = '01D06079861D79F99F'
b = '0F97A3'


def cal(i):
    ret = 0
    for k in range(len(i)):
        tmp = pow(2, k)
        if i[::-1][k] == '1':
            ret += tmp
    return ret


def bit(i):
    ret = ''
    for j in range(3, -1, -1):
        ret += '1' if i & (1 << j) else '0'

    return ret


res = ''
for k in a:
    res += bit(int(k, 16))

for i in range(len(res) // 7 + 1):
    print(cal(res[i * 7:(i + 1) * 7]))