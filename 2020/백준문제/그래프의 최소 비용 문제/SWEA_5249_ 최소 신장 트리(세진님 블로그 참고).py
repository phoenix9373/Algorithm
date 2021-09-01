import sys
sys.stdin = open('input.txt', 'r')


def MST_PRIM(G ,s): # G: 그래프, s: 시작점.
    key = [float('inf') for _ in range(V + 1)]
    pi = [None for _ in range(V + 1)]
    visited = [False for _ in range(V + 1)]
    key[s] = 0

    for _ in range(V + 1): # 정점의 개수만큼 반복.
        # 최소 key 찾기
        min_key = float('inf')
        min_idx = -1
        for i in range(V + 1):
            if key[i] < min_key and not visited[i]:
                min_idx = i
                min_key = key[i]
        # 방문 & 주변 key 값 갱신
        visited[min_idx] = 1
        for next_v, next_w in G[min_idx]:
            if next_w < key[next_v] and not visited[next_v]:
                key[next_v] = next_w
                pi[next_v] = min_idx
    return sum(key)


for tc in range(1, 1 + int(input())):
    V, E = map(int, input().split())
    my_graph = {}
    for _ in range(E):
        n1, n2, w = map(int, input().split())
        if n1 not in my_graph:
            my_graph[n1] = set()
        if n2 not in my_graph:
            my_graph[n2] = set()
        my_graph[n1].add((n2, w))
        my_graph[n2].add((n1, w))
    ans = MST_PRIM(my_graph, 0)
    print('#{} {}'.format(tc, ans))