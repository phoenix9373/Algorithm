import sys
sys.stdin = open('input.txt', 'r')

for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    grid = []
    for i in range(N):
        temp = list(map(int, input().split()))
        grid.append(temp)

    home = []
    for i in range(N):
        for j in range(N):
            if grid[i][j]:
                home.append([i, j])

    ans = 1
    for k in range(1, N+1): # 왜 N + 2까지만했지..?
        for i in range(N):
            for j in range(N):
                cnt = 0
                for h in home: # 범위 내에 있는 집들을 센다.
                    if abs(i - h[0]) + abs(j - h[1]) < k:
                        cnt += 1
                if cnt*M - (k**2 + (k-1)**2) >= 0 and ans < cnt:
                    ans = cnt
    print('#{} {}'.format(tc, ans))