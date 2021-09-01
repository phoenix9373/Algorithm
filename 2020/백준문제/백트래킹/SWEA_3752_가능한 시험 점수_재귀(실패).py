# 제한시간 초과.

def comb(idx, cumsum=0):

    if idx == N:
        global ret
        ret.add(cumsum)
        return

    overlap = 0

    comb(idx + 1, cumsum + scores[idx])    # 선택
    comb(idx + 1, cumsum)                  # 미선택

for tc in range(1, int(input()) + 1):
    N = int(input())
    visited = [0] * N
    scores = list(map(int, input().split()))
    ret = set()
    comb(0)

    print('#{} {}'.format(tc, len(ret)))