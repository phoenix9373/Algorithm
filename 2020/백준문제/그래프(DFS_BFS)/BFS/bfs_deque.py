from collections import deque

N, E = map(int, input().split())

graph = [[] * (N + 1) for _ in range(N + 1)]

for _ in range(E):
    s, e = map(int, input().split())
    graph[s].append(e)
print(graph)
visited = [0] * (N + 1)

def BFS(v):

    q = deque() # q = deque()
    q.append(v)

    visited[v] = 1

    while q:
        tmp = q.popleft() # q.popleft()
        print(tmp, end=' ')
        for w in graph[tmp]:
            if visited[w] == 0:
                q.append(w)
                visited[w] = 1

BFS(1)

'''
7 8
1 2
1 3
2 4
2 5
4 6
5 6
6 7
3 7
'''
