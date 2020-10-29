import sys
sys.stdin = open('input.txt', 'r')

for tc in range(1, int(input()) + 1):
    N = int(input())
    times = sorted([list(map(int, input().split())) for _ in range(N)], key=lambda x: (x[1], x[0]))
    ans = 0

    t = times[0][1]
    for i in range(N):
        if i == 0:
            ans += 1
            continue
        else:
            s, e = times[i]
            if s >= t:
                ans += 1
                t = e
    print('#{} {}'.format(tc, ans))