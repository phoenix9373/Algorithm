def bfs(v):
    q = []
    q.append(v)
    visited[v] = 1

    while q:
        t = q.pop(0)

        for w in adj_list[t]:
            if visited[w] == 0:
                q.append(w)
                visited[w] = visited[t] + 1


def find_max_idx(arr):
    max_val = 0
    max_idx = 0
    for idx, i in enumerate(arr):
        if i >= max_val:
            max_val = i
            max_idx = idx
    return max_idx


for tc in range(1, 11):
    n, start = map(int, input().split())
    num_list = list(map(int, input().split()))
    adj_list = [[] for _ in range(101)]
    visited = [0] * 101
    for i in range(n//2):
        s = num_list[i*2]
        e = num_list[i*2 + 1]
        if e not in adj_list[s]:
            adj_list[s].append(e)

    bfs(start)
    result = find_max_idx(visited)
    print('#{} {}'.format(tc, result))