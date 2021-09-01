from collections import deque

N, K = map(int, input().split())
visited = [0] * 100001

def bfs(v):

    q = deque()
    q.append(v)
    visited[v] = 1

    while q:
        t = q.popleft()
        if t == K:
            break

        for w in [t-1, t+1, 2 * t]:
            if 0 <= w <= 100000 and visited[w] == 0:
                q.append(w)
                visited[w] = visited[t] + 1

bfs(N)
print(visited[K] - 1)