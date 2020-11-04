byte = input()

for i in range(len(byte) // 7):
    tmp = byte[i*7:(i+1)*7]
    res = 0
    for e, b in enumerate(tmp[::-1]):
        if b == '1':
            res += pow(2, e)
    print(res)