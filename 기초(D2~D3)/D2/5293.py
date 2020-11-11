def count(n):
        for i in range(1<<n):
            t = ''
            for j in range(n):
                if i & (1<<j):
                    t += '1'
                else:
                    t += '0'
            l = [t[k:k+2] for k in range(len(t)-1)]
            l_count = [l.count(m) for m in ['00', '01', '10', '11']]
            if l_count[0]==num[0] and l_count[1]==num[1] and l_count[2]==num[2] and l_count[3]==num[3]:
                return t
        return 'impossible'
for c in range(1, int(input())+1):
    num = list(map(int, input().split()))
    x = sum(num) + 1
    print(f'#{c} {count(x)}')
