'''7 8
1 2
1 3
2 4
2 5
4 6
5 6
6 7
3 7'''

V, E = map(int, input().split())
input_arr = [list(map(int, input().split())) for _ in range(E)]
G = [[0] * (V + 1) for _ in range(V + 1)]
visited = [0] * (V + 1)
track = []

for k in range(E):
    i, j = input_arr[k][0], input_arr[k][1]
    G[i][j] = G[j][i] = 1

def bfs(v):
    q = []
    visited[v] = 1
    q.append(v)

    while q:
        t = q.pop(0)
        track.append(t)

        for i in range(1, V + 1):
            if G[t][i] == 1 and visited[i] == 0:
                q.append(i)
                visited[i] = visited[t] + 1
bfs(1)
print(track)