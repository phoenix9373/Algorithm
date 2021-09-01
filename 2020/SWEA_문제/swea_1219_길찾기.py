def dfs(v):
    visited[v] = 1
    adj_list = [idx for idx, i in enumerate(G[v]) if i==1]
    for j in adj_list:
        if visited[j] == 0:
            dfs(j)

for _ in range(10):
    tc, n = map(int, input().split())
    N = 100 # 정점 개수
    arr = list(map(int, input().split())) # 간선
    G = [[0] * N for _ in range(N)]

    for i in range(n): # 인접행렬에 데이터 저장.
        s, e = arr[i*2], arr[i*2+1]
        G[s][e] = 1
    visited = [0] * 100
    dfs(0)
    print(visited[-1])
