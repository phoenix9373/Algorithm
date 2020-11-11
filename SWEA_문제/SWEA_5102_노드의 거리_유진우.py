def bfs(v, e_v):
    cnt = 0
    q = []
    visited[v] = 1
    q.append(v)

    while q:
        t = q.pop(0)

        for w in adj_list[t]:
            if visited[w] ==0 and w == e_v:
                return visited[t]

            if visited[w] == 0:
                q.append(w)
                visited[w] = visited[t] + 1
    return 0

for tc in range(1, int(input()) + 1):
    V, E = map(int, input().split())
    adj_list = [[] for _ in range(V + 1)]

    for _ in range(E):
        s, e = map(int, input().split())
        adj_list[s].append(e)
        adj_list[e].append(s)

    S, G = map(int, input().split())
    visited = [0] * (V + 1)
    result = bfs(S, G)
    print('#{} {}'.format(tc, result))