import sys

sys.stdin = open('input.txt', 'r')


def dfs(idx, cumsum, bi, bj):
    global ans
    if cumsum > ans:
        return

    if idx == N:
        cumsum += abs(bi - e[0]) + abs(bj - e[1])
        if cumsum < ans:
            ans = cumsum
        return

    for i in range(N):
        if visited[i] == 0:
            visited[i] = 1
            tmp = abs(bi - arr[i][0]) + abs(bj - arr[i][1])
            dfs(idx + 1, cumsum + tmp, arr[i][0], arr[i][1])
            visited[i] = 0


for tc in range(1, int(input()) + 1):
    N = int(input())
    info = list(map(int, input().split()))
    s = [info[0], info[1]]
    e = [info[2], info[3]]
    arr = [[info[i], info[i + 1]] for i in range(4, len(info), 2)]
    visited = [0] * N

    ans = pow(2, 30)
    dfs(0, 0, s[0], s[1])
    print('#{} {}'.format(tc, ans))