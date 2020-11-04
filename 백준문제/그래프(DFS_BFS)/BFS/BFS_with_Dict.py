'''
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
'''
def bfs(v):

    Q = []

    # enQ
    Q.append(v)
    visited[v] = 1
    print(v, end=' ')
    while Q: # Q가 없을 때까지.
        v = Q.pop(0)
        for w in G[v]:
            if not visited[w]:
                Q.append(w)
                visited[w] = visited[v] + 1 # v를 기준으로 얼마나 떨어져있는지 확인가능.
                print(w, end=' ')


V, E = map(int, input().split())
temp = list(map(int, input().split()))
visited = [0] * (V + 1)

# 인접리스트
# G = [[] for _ in range(V + 1)] # [[], [], [], [], [], [], [], []]
G = {i:[] for i in range(1, V + 1)}
for i in range(E):
    s, e = temp[i*2], temp[i*2 + 1]
    G[s].append(e)
    G[e].append(s)

print(G) # [[], [2, 3], [1, 4, 5], [1, 7], [2, 6], [2, 6], [4, 5, 7], [6, 3]]
bfs(1)
print()
# 1에서 가장 멀리있는 정점의 번호는 무엇이고, 몇 칸 떨어져 있을까요? visited 이용.
# 시작점을 기준으로 visited의 값이 얼마나 떨어져있는지 표현 가능.
maxI = 0
for i in range(1, V + 1):
    if visited[maxI] < visited[i]:
        maxI = i
print(maxI, visited[maxI] - 1)