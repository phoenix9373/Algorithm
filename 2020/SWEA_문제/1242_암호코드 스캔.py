import sys
sys.stdin = open('input.txt', 'r')

hex_decoder = {'0': '0000', '1': '0001', '2': '0010', '3': '0011',
               '4': '0100', '5': '0101', '6': '0110', '7': '0111',
               '8': '1000', '9': '1001', 'A': '1010', 'B': '1011',
               'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111'}

decoder = {'211': 0, '221': 1, '122': 2, '411': 3, '132': 4, '231': 5, '114': 6, '312': 7, '213': 8, '112': 9}

for tc in range(1, int(input()) + 1):

    N, M = map(int, input().split())
    hex_codes = []
    ans = 0

    # 16진수를 담은 줄만 가져옴.
    for _ in range(N):
        row = input()
        if row not in hex_codes and row != '0' * M:
            hex_codes.append(row)

    # 2진수 변환.
    binary_codes = []
    for line in hex_codes:
        tmp = ''
        for c in line:
            tmp += hex_decoder[c]
        if tmp not in binary_codes:
            binary_codes.append(tmp)
    # print('#{} {}'.format(tc, binary_codes))
    for code in binary_codes:
        j = M * 4 - 1
        # while문에서 암호코드 전체 가져오기.
        res = []
        arr = []
        while j > -1:
            c1 = c2 = c3 = c4 = 0
            if code[j] == '1':
                while code[j] == '1':
                    c4 += 1
                    j -= 1
                while code[j] == '0':
                    c3 += 1
                    j -= 1
                while code[j] == '1':
                    c2 += 1
                    j -= 1
            else:
                j -= 1
                continue
            j -= 1  # 2번째 1이 나오면 그 다음은 상관없음.
            # c1 ~ c4 값 나옴. 비율대로 나눠서 값을 더하자.
            key = ''.join(list(map(lambda x: str(int(x / min(c2, c3, c4))), [c2, c3, c4])))
            arr.append(decoder[key])
            if len(arr) != 0 and len(arr) % 8 == 0:
                t = len(arr) // 8
                res.append(arr[(t-1)*8:t*8])
        ret = list(set([''.join(map(str, i)) for i in res]))
        print('ret: ', ret)
        for i in range(len(ret)):
            print('ret[i]: ', ret[i])
            k = list(map(int, x.split()))
            print(k)
            l_sum = (k[0] + k[2] + k[4] + k[6]) + (k[1] + k[3] + k[5] + k[7]) * 3
            if l_sum % 10 == 0:
                ans += sum(k)

    print('#{} {}'.format(tc, ans))