for tc in range(1, int(input().strip()) + 1):
    line = list(input())
    tmp = ''
    temp_list = []
    for i in range(len(line)):
        if i % 3 == 1 and line[i] != '0':
            tmp += line[i]
        elif i % 3 == 2:
            tmp += line[i]
            temp_list.append(int(tmp))
            tmp = ''
        elif i % 3 == 0:
            temp_list.append(line[i])
    n = 13
    result = 0
    check = {i:[] for i in 'SDHC'}
    for i in range(int(len(temp_list)/2)):
        k = temp_list[i*2]
        v = temp_list[i*2 + 1]
        if v in check[k]:
            result = 'ERROR'
            break
        else:
            check[k].append(v)
    print('#{}'.format(tc), end=' ')
    if result:
        print(result)
    else:
        for i in check:
            print(n - len(check[i]), end=' ')
            if i == 'C':
                print()

'''3
S01D02H03H04
H02H10S11H02
S10D10H10C01'''