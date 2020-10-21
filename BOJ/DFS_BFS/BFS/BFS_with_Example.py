'''
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
'''
def bfs(v): # v는 시작점
    # 큐, 방문
    Q = []
    visited = [0] * (V + 1)
    # enQ(v), visited
    Q.append(v)
    visited[v] = 1

    # 큐가 비어있지 않은 동안,
    while len(Q) != 0:
        # v = deQ()
        v = Q.pop(0)
        # v의 인접한 정점(w), 방문 안한 정점이면,
        for w in range(1, V + 1):
            # enQ(w), 방문처리(w)
            if G[v][w] == 1 and visited[w] == 0:
                Q.append(w)
                visited[w] = visited[v] + 1




# 입력 -> 인접행렬로 만들기
V, E = map(int, input().split())
temp = list(map(int, input().split()))

# 인접행렬 초기화.
G = [[0] * (V + 1) for _ in range(V + 1)]
# 간선 정보로 인접행렬 채우기.
for i in range(E):
    s, e = temp[2*i], temp[2*i + 1]
    G[s][e] = 1
    G[e][s] = 1

for i in range(1, V+1):
    print('{} {}'.format(i, G[i]))

