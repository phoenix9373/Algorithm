import sys
n = int(sys.stdin.readline())
line = int(sys.stdin.readline())

arr = [list(map(int, sys.stdin.readline().split())) for _ in range(line)] # 간선 페어
G = [[0] * (n + 1) for _ in range(n+1)] # 인접행렬
visited = [0] * (n + 1) # 방문 여부. 인덱스를 맞추기 위해 n + 1로 할당.

for item in arr:
    i, j = item[0], item[1]
    G[i][j] = 1
    G[j][i] = 1

def dfs(v): # v는 시작점
    visited[v] = 1 # 방문여부

    for w in range(1, n+1):
        if G[v][w] == 1 and visited[w] == 0: # v와 연결된 간선이고, 방문하지 않은 인접점에 대해
            dfs(w)

dfs(1)
print(sum(visited) - 1)