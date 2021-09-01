import sys
from collections import deque

def bfs(v):
    q = deque()
    q.append(v)

    while q:
        p = q.popleft()
        for c in adj_list[p]:
            if parent[c] == 0:
                q.append(c)
                parent[c] = p


N = int(sys.stdin.readline())
adj_list = [[] for _ in range(N + 1)]

for _ in range(N - 1):
    i, j = map(int, sys.stdin.readline().strip().split())
    adj_list[i].append(j)
    adj_list[j].append(i)

parent = [0] * (N + 1)
parent[1] = -1
bfs(1)
print(*parent[2:], sep='\n')