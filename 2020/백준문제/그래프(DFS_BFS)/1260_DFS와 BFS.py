# 그래프를 DFS, BFS로 탐색한 결과 출력
# 방문할 수 있는 정점이 여러 개인 경우, 번호가 작은 것을 먼저 방문.
# 더 이상 방문할 곳이 없는 경우 종료.
import sys
from collections import deque


def bfs(v):
    q = deque()
    q.append(v)
    visited_2[v] = 1

    while q:
        t = q.popleft()
        print(t, end=' ')
        for w in sorted(adj_list[t]):
            if visited_2[w] == 0:
                q.append(w)
                visited_2[w] = 1


def dfs(v):

    visited_1[v] = 1
    print(v, end=' ')
    for w in sorted(adj_list[v]):
        if visited_1[w] == 0:
            dfs(w)


# 1. 입력
N, M, V = map(int, sys.stdin.readline().split())

# 2. 인접행렬
adj_list = [[] for _ in range(N + 1)]
for _ in range(M):
    s, e = map(int, sys.stdin.readline().split())
    adj_list[s].append(e)
    adj_list[e].append(s)

visited_1 = [0] * (N + 1) # 방문 체크
dfs(V)
print()
visited_2 = [0] * (N + 1) # 방문 체크
bfs(V)