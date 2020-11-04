import sys
sys.stdin = open('input.txt', 'r')
from collections import deque


def bfs(s):
    q = deque()
    q.append(s)
    visited[s] = 1

    while q:
        t = q.popleft()
        for w in adj[t]:
            if visited[w] == 0:
                visited[w] = visited[t] + 1
                q.append(w)


for tc in range(1, 11):
    N, S = map(int, input().split())
    info = list(map(int, input().split()))
    adj = [[] for _ in range(101)]
    visited = [0] * (101)
    for i in range(0, len(info), 2):
        s, e = info[i], info[i + 1]
        adj[s].append(e)
    bfs(S)
    M = max(visited)
    for i in range(len(visited) - 1, -1, -1):
        if visited[i] == M:
            ans = i
            break
    print('#{} {}'.format(tc, ans))