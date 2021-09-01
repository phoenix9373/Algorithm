from collections import deque

def bfs(v):
    q = deque()
    q.append(v)
    if visited[v] == 0: # 0이면 1로 초기화해주고, 아니면 1 이상이므로 둔다.
        visited[v] = 1

    while q:
        t = q.popleft()

        for w in adj_list[t]:
            if visited[w] == 0:
                q.append(w)
                visited[w] = visited[t] + 1

for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    adj_list = [[] for _ in range(N + 1)]
    for _ in range(M):
        s, e = map(int, input().split())
        adj_list[s].append(e)
        adj_list[e].append(s)
    visited = [0] * (N + 1)
    for i in range(1, N + 1):
        bfs(i)
    cnt = visited.count(1) # 첫 방문한 노드를 센다.
    print('#{} {}'.format(tc, cnt))