from collections import deque


# 백만 이하.
# 4가지 연산
# +1, -1, *2, -10
# 최소 연산 횟수.
def sol(n):
    global ans

    q = deque()
    q.append([n, 0])
    check = {}
    while q:
        t, cnt = q.popleft()

        if check.get(t, 0): continue
        check[t] = 1

        if t == M: return cnt

        if 0 < t + 1 <= K:
            q.append([t + 1, cnt + 1])
        if 0 < t - 1 <= K:
            q.append([t - 1, cnt + 1])
        if 0 < t * 2 <= K:
            q.append([t * 2, cnt + 1])
        if 0 < t - 10 <= K:
            q.append([t - 10, cnt + 1])
    return 0


for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())  # N은 처음, M은 연산 후.
    K = pow(10, 6)
    ans = sol(N)
    print('#{} {}'.format(tc, ans))