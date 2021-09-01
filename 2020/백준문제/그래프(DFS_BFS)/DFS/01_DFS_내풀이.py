# APS_응용 -> 그래프 -> 'DFS 알고리즘 - 재귀' - 280 page
# 1. 재귀 / 2. 반복
n, m = map(int, input().split()) # 정점, 간선
arr = [list(map(int, input().split())) for _ in range(m)] # 2차원 배열 생성. 각 1차원 요소는 간선.
visited = {i:False for i in range(1, n+1)} # 모든 정점에 대해 False. 방문 여부.
stack = [] # 경로 저장.

def adjacent(G, v): # 인접 경로 반환.
    ad_list = [] # G = arr에서 v 정점에 대해 간선으로 연결된 점 w의 집합.
    for line in G: # line은 간선.
        if v in line: # v가 있는 간선에 대해서만.
            for w in line: # line 안에 두 점.(본인 포함 가능)
                if v in line and w != v: # v와 연결되어 있는 점. 자기 자신 제외.
                    ad_list.append(w) # v가 1이고, [1, 2], [3, 1] 등이 있으면 2, 3이 ad_list에 추가됨.
    return ad_list

def dfs_recursive(G, v): # G에는 arr가 들어간다.
    visited[v] = True # 방문한 정점에 대해 True 값을 부여.
    stack.append(v) # # 방문 경로 저장.
    for w in adjacent(G, v):
        if visited[w] == False and adjacent(G, w): # 해결: adjacent가 있는 경우만 밑에걸 돌린다.
            return dfs_recursive(G, w)
        else:

            # 인접점이 모두 visited=True인 경우 None을 return. None return 시 상위 함수에서도 None을 return 하면서 끝남.
                                       # 즉, 6의 경우 인접점이 (4, 5, 7)인데 5에서 None을 return하면서 끝나므로, 6에서는 visited=False인 7을 가지 않고,
                                       # dfs_recursive(arr, 5)에서 return된 None을 다시 return 하면서 끝난다.
                                       # 그래서 stack 경로에서 1, 2, 4, 6, 5까지만 출력되고 끝난 것이다.
dfs_recursive(arr, 1)
print(stack)