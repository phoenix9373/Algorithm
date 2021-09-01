# 다익스트라(Dijkstra) 알고리즘
# DP를 활용한 최단 경로 탐색 알고리즘.
# 특정 하나의 정점에서 다른 모든 정점으로 가는 최단 경로 탐색.
# 음의 간선 포함하지 않음.
# IDEA: 최단 거리는 여러 개의 최단 거리로 이루어져 있다.

V, E = map(int, input().split())
S = int(input())
G = [[] for _ in range(V + 1)]

for _ in range(E):
    u, v, w = map(int, input().split())
    G[u].append((v, w))


def dijkstra(graph, start):
    D = [float('inf') for _ in range(V + 1)]
    visited = [0] * (V + 1)
    D[start] = 0

    for _ in range(1, V + 1):
        min_idx = -1
        min_val = float('inf')

        for i in range(V + 1):
            if not visited[i] and D[i] < min_val:
                min_idx = i
                min_val = D[i]

        visited[min_idx] = 1
        for w, value in G[min_idx]:
            if not visited[w] and D[min_idx] + value < D[w]:
                D[w] = D[min_idx] + value

    return D


ans = dijkstra(G, S)
for c in ans[1:]:
    if c == float('inf'):
        print('INF')
    else:
        print(c)