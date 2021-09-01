# backtracking
def dfs(tmp, n, total):
    global maxV
    # 숫자가 작아서 가지치기 따로 안함
    if n == M:
        if total > maxV:
            maxV = total
    else:
        if tmp + 1 <= N:
            dfs(tmp + 1, n + 1, total + stones[tmp + 1])
        if tmp + 2 <= N:
            dfs(tmp + 2, n + 1, total + stones[tmp + 2])

# 테스트케이스 T
T = int(input())
for tc in range(1, T + 1):
    # 정보 입력
    N, M = map(int, input().split())
    # index 편하게 맞춰주기
    stones = [0] + list(map(int, input().split()))
    maxV = 0
    dfs(0, 0, 0)
    print('#{} {}'.format(tc, maxV))