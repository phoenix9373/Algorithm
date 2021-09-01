n, m = map(int, input().split())
arr = [i for i in range(1, n + 1)] # 1, 2, ..., n
sel = [0] * m
visited = [0] * n

def perm(idx):

    if idx == m:
        print(*sel)
        return

    for i in range(n):
        if visited[i] == 0:
            sel[idx] = arr[i]
            visited[i] = 1
            perm(idx + 1)
            visited[i] = 0

perm(0)