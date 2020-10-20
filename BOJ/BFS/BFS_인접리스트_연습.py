def BFS(a):
    q = []
    q.append(a)
    visited[a] = 1 # 시작점 방문 체크

    while q: # 비어있지 않을 때까지.
        t = q.pop(0)
        print(t, end=' ')

        for w in L[t]:
            if visited[w] == 0:
                q.append(w)
                visited[w] = visited[t] + 1
    print() # 구분.

V, E = map(int, input().split())
# 인접리스트 생성
L = [[] for _ in range(V + 1)]
for k in range(E):
    s, e = map(int, input().split())
    L[s].append(e)
    L[e].append(s)
visited = [0] * (V + 1)

BFS(1)
print(visited)