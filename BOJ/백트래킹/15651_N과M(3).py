n, m = map(int, input().split())
arr = [i for i in range(1, n + 1)]
sel = [0] * m

def perm(idx):

    if idx == m:
        print(*sel)
        return

    for i in range(n):
        sel[idx] = arr[i]
        perm(idx + 1)

perm(0)