import sys
sys.stdin = open('input.txt', 'r')


# 완전 탐색.
# 그리디
# DP
def dfs(s, total):
    global ans
    if total == 0:
        return
    elif total <= ans:
        return

    if s == N:
        if total > ans:
            ans = total
        return

    for k in range(N):
        if visited[k] == 0:
            visited[k] = 1
            dfs(s + 1, total*(arr[s][k] / 100))
            visited[k] = 0


for tc in range(1, int(input()) + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N
    ans = 0
    dfs(0, 1)

    print('#{} {:.6f}'.format(tc, round(ans*100, 6)))