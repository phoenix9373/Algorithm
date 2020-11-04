for c in range(1, int(input())+1):
    t = ' '.join(input()).split()
    n = int(input())
    p = list(map(int, input().split()))
    l = ''
    for i in p:
        if i:
            t[i-1] += '-'
        else:
            l += '-'
    r = l + ''.join(t)
    print(f'#{c} {r}')