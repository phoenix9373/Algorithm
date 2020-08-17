import sys
sys.stdin = open('input.txt', 'r')
for c in range(1, int(input())+1):
    n = int(input())
    f = [int(input()) for _ in range(n)]
    cnt = 0
    while len(f) > 1:
        d = f[1] - f[0]
        a = f[1]
        while 1:
            if a in f:
                f.remove(a)
            a += d
            if a > f[-1]:
                cnt += 1
                break
    
    print(f'#{c} {cnt}')