import sys
n = int(sys.stdin.readline())

arr = [list(map(int, sys.stdin.readline().strip())) for _ in range(n)]

visited = [[0] * n for _ in range(n)] # 방문 여부 생성.

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def dfs(v): # v는 2차원 배열에서의 시작점. [i, j]
    global cnt
    i, j = v[0], v[1]
    cnt += 1
    visited[i][j] = 1

    for k in range(4):
        ni = i + dx[k]
        nj = j + dy[k]

        if 0 <= ni < n and 0 <= nj < n and visited[ni][nj] == 0 and arr[ni][nj] == 1:
            dfs([ni, nj])
count = []
for i in range(n):
    for j in range(n):
        cnt = 0
        if visited[i][j] == 0 and arr[i][j] == 1:
            dfs([i, j])
            count.append(cnt)

print(len(count))
print(*sorted(count), sep='\n')