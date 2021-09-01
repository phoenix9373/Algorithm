from collections import deque

n, m, k, x = map(int, input().split())
adj = [[] for _ in range(n + 1)]
visited = [0] * (n + 1)


for _ in range(m):
    s, e = map(int, input().split())
    adj[s].append(e)
print(adj)
def bfs(v, K):

    q = deque()
    q.append(v)
    visited[v] = 1
    result = []

    while q:
        t = q.popleft()

        for w in adj[t]:
            if visited[w] == 0:
                q.append(w)
                visited[w] = visited[t] + 1
                if visited[w] - 1 == K:
                    result.append(w)

    return result

ans = bfs(x, k)
if ans:
    print(*ans, sep='\n')
else:
    print(-1)