import sys
sys.stdin = open('input.txt', 'r')
for tc in range(1, int(input())+1):
    n, r = map(int, input().split())
    x = 1234567891
    if n-r < r:
        r = n-r
    ncr = 1.0
    for i in range(n, n-r, -1):
        ncr = ncr*i
    for j in range(r, 0, -1):
        ncr = ncr/j
    if ncr > x:
        result = ncr % x
    else:
        result = ncr
    print(f'#{tc} {int(result)}')