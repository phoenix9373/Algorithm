N, M = map(int, input().split())
arr = sorted(list(map(int, input().split())))
sel = [0] * M

def perm(idx):

    if idx == M:
        print(*sel)
        return

    overlap = 0 # 같은 depth 에서 중복 방지. 정렬된 상태.
    for i in range(N):
        if overlap != arr[i]:
            overlap = arr[i]
            sel[idx] = arr[i]
            perm(idx + 1)

perm(0)