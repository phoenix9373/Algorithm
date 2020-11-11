import sys
sys.stdin = open('input.txt', 'r')


def dfs(v, cnt, total):
    global ans
    if ans <= total:
        return

    if cnt == N - 1:
        if total + arr[v][0] < ans:
            ans = total + arr[v][0]
        return

    for i in range(N):
        if visited[i] == 0:
            visited[i] = 1
            dfs(i, cnt + 1, total + arr[v][i])
            visited[i] = 0


for tc in range(1, int(input()) + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = pow(2, 30)
    visited = [0] * N
    visited[0] = 1
    dfs(0, 0, 0)

    print('#{} {}'.format(tc, ans))
#
# 3
# 3
# 0 18 34
# 48 0 55
# 18 7 0
# 4
# 0 83 65 97
# 82 0 78 6
# 19 19 0 82
# 6 34 94 0
# 5
# 0 9 26 85 42
# 14 0 84 31 27
# 58 88 0 16 46
# 83 61 94 0 17
# 40 71 24 38 0