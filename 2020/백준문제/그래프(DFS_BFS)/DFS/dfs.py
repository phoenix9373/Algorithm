N = 10
visited = [0] * N
stack = []
G = [[0] * (N + 1) for _ in range(N + 1)]

def dfs(v):
    visited[v] = 1

    for w in G[v]:
        if w == 1 and visited[w] == 0:
            stack.append(v)
