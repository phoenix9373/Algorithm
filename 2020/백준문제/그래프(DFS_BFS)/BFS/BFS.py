# 1. enQ 시 방문처리
n = 3
G = [[0] * (n + 1) for _ in range(n + 1)]
def BFS(G, v):                      # G는 인접행렬, v는 시작점

    visited = [0] * (n + 1)         # n: 정점의 개수. 값과 동일한 위치의 index를 사용하기 위해 +1.
    q = []                          # 큐 생성.

    q.append(v)                     # 시작정점 v를 enQueue
    visited[v] = 1                  # 방문처리

    while len(q) != 0:              # 비어있을 때까지 반복.
        t = q.pop(0)                # q의 가장 앞에 있는 요소 enQ()로 시작점 지정.

        for w in range(n):          # i는 시작점 v에 인접한 접점.
            if G[v][w] == 1 and visited[w] == 0:
                q.append(w)         # 방문하지 않고, v에 인접했으면 q에 추가.
                visited[w] = visited[t] + 1 # 시작점에서 얼마나 떨어져있는지 알기 위해 이전 방문지에서 +1을 한다.