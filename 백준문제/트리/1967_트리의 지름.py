import sys
from collections import deque


N = int(sys.stdin.readline())
tree = [[] for _ in range(N + 1)]

for _ in range(N - 1):
    p, c, w = map(int, sys.stdin.readline().strip().split())
    tree[p].append([c, w])
    tree[c].append([p, w])


def bfs(v, visited):
    q = deque()
    q.append(v)
    visited[v[0]] = v[1]

    while q:
        t = q.popleft()
        p, pw = t[0], t[1]

        for c, w in tree[p]:
            if visited[c] == 0:
                q.append([c, w])
                visited[c] = visited[p] + w


    return visited


result = [0] * (N + 1)
bfs([1, 0], result)
max_index = result.index(max(result))

result_2 = [0] * (N + 1)
bfs([max_index, 0], result_2)
print(max(result_2))