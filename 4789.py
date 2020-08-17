import sys
sys.stdin = open('input.txt', 'r')
for c in range(1, int(input())+1):
    num = list(map(int, ' '.join(input()).split()))
    s = 0
    cnt = 0
    for idx, i in enumerate(num):
        if s > idx:
            s += i
        else:
            cnt += idx - s
            s += idx - s + i
    print(f'#{c} {cnt}')
