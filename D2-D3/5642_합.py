import sys
sys.stdin = open('input.txt', 'r')
for t in range(1, int(input())+1):
    n = int(input())
    d = list(map(int, input().split()))
    m = d[0]
    for i in range(1, n):
        if (d[i] + d[i-1] > 0) and d[i-1] > 0:
            d[i] = d[i] + d[i-1]
        if m < d[i]:
            m = d[i]
    print(f'#{t} {m}')