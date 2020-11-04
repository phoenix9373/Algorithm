"""
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
"""

def dfs(v):
    global cnt

    # 방문체크
    visited[v] = 1
    print(v, end= " ")
    # v의 인접한 정점 중에서 방문하지 않은 정점을 재귀호출
    for w in range(1, N+1): # 모든 인접점에 대해 반복문으로 접근하므로, 모두 접근함.
        if G[v][w] == 1 and visited[w] == 0:
            dfs(w)

# 정점, 간선
N, E = map(int, input().split())

# 간선들
tmp = list(map(int, input().split()))

# 인접행렬
G = [[0] * (N+1) for _ in range(N+1)]

# 방문체크
visited = [0] * (N+1)

# 간선들을 인접행렬에 저장
for i in range(E):
    s, e = tmp[2*i], tmp[2*i+1]
    G[s][e] = 1
    G[e][s] = 1

dfs(1)