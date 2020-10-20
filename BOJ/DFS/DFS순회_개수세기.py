"""
7
0000000
0000000
0011100
0010111
0110010
0011100
0000000
"""

n = int(input())
arr = [list(map(int, list(input()))) for _ in range(n)]
visited = [[0] * n for _ in range(7)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def dfs(v):
    i, j = v[0], v[1]
    visited[i][j] = 1

    for k in range(4):
        ni = i + dx[k]
        nj = j + dy[k]
        if 0 <= ni < n and 0 <= nj < n and arr[ni][nj] == 1 and visited[ni][nj] == 0:
            w = [ni, nj]
            dfs(w)

dfs([2,2])
cnt = 0
for i in range(n):
    for j in range(n):
        if visited[i][j] == 1:
            cnt += 1
print(visited)
print(cnt)