def djikstra(G):
    key = [float('inf')] * (N + 1)
    path = [None] * (N + 1)
    visited = [0] * (N + 1)
    key[0] = 0

    for _ in range(N + 1):
        min_idx = -1
        min_val = float('inf')

        for i in range(N + 1):
            if not visited[i] and key[i] < min_val:
                min_val = key[i]
                min_idx = i

        visited[min_idx] = 1
        for v, val in G[min_idx]:
            if not visited[v] and key[min_idx] + val < key[v]:
                key[v] = key[min_idx] + val
                path[v] = min_idx
    return key, path


for tc in range(1, int(input()) + 1):
    N, E = map(int, input().split())
    graph = {}
    for _ in range(E):
        u, v, w = map(int, input().split())
        if u not in graph:
            graph[u] = set()
        if v not in graph:
            graph[v] = set()
        graph[u].add((v, w))
        graph[v].add((u, w))

    k, p = djikstra(graph)
    print(k)
    print(p)
    print('----------------------------')
    # print('#{} {}'.format(tc, my_graph))

# 1
# 2 3
# 0 1 1
# 0 2 6
# 1 2 1