# DFS는 Stack을 활용한다.
# 깊은 곳까지 갔다가 막히면, 가장 마지막에 만났던 갈림길 간선이 있는 정점으로 돌아옴.

# 1. 시작 정점 v를 결정하여 방문
# 2. 방문하지 않은 정점 w가 있으면, v를 스택에 push하고 w를 방문
# 3. w를 v로 하여 반복.
# 4. 방문하지 않은 정점 w가 없으면, 탐색의 방향을 바꾸기 위해 스택을 pop하여 받고
# 5. 가장 마지막 방문 정점을 v로 하여 다시 반복.

# 중요: 각 정점이 연결되어 있는 것을 어떻게 표현? => 인접행렬 활용. 또는 2차원 배열 활용.

# 방문, 스택 초기화 / 방문은 "상태 정보"라고 하자.
n = 10 # 정점 개수.
visited = [0] * n # 각 정점을 방문 했는지 여부.
stack = [] # 각 정점에 대한 것이 아니라 경로를 저장.
G = [[0] * (n+1) for _ in range(n+1)]

# DFS 함수가 호출될 때, 방문 시작 정점 v가 정해진다.
def DFS(v):
    visited[v] = 1

    for w in G[v]:
        if (w == 1) and visited[w] == 0:
            stack.append(v)
            DFS(w)
    v = stack.pop()
    DFS(v)