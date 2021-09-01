# bit_mask로 하는 방법도 있다.

arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
N = 3

sel = [0] * N # 사용.
visited = [[0] * N for _ in range(N)]

def perm(idx, row):
    if row == N:
        print(sel)
        print()
        return

    for i in range(N):
        if not visited[row][i]:
            sel[idx] = arr[row][i]
            for j in range(N):
                visited[j][i] = 1
            perm(idx+1, row+1)
            for j in range(N):
                visited[j][i] = 0

perm(0, 0)