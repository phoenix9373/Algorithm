# 제한시간 초과.
# 부분 집합을 구하기는 하는데, 이전에 했던 건 빼고.
# 중복을 피하자는거지.
def comb(idx, M):

    if idx == M:
        global ret, sel
        ret.add(sum(sel))
        return

    overlap = 0 # 같은 depth에서 생기는 중복을 피함.
    for i in range(N):
        if scores[i] != overlap and visited[i] == 0:
            overlap = scores[i]
            sel[idx] = scores[i]
            visited[i] = 1
            comb(idx + 1, M)
            visited[i] = 0


for tc in range(1, int(input()) + 1):
    N = int(input())
    scores = list(map(int, input().split()))
    visited = [0] * N
    ret = set()
    for i in range(1, N + 1):
        sel = [0] * i
        comb(0, i)
    print('#{} {}'.format(tc, len(ret) + 1))