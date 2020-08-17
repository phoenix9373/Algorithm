# 31: 1, 3, 5, 7, 8, 10, 12
# 30: 4, 6, 9, 11
for c in range(1, int(input())+1):
    cnt = 4
    m, d = map(int, input().split())
    dic = {}
    for k in range(1, 13):
        if k == 2:
            dic[k] = 29
        elif k in [4, 6, 9, 11]:
            dic[k] = 30
        else:
            dic[k] = 31
    if m > 1:
        for i in range(1, m):
            cnt += dic[i]
        cnt += d-1
    else:
        cnt += d-1
    print(f'#{c} {cnt%7}')