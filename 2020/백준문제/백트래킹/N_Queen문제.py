# 백트래킹 절차
# 1. 상태 공간 Tree의 깊이 우선 탐색 실시
# 2. 각 노드가 유망한지 점검
# 3. 만일 그 노드가 유망하지 않으면, 그 노드의 부모 노드로 돌아가서 검색을 계속.

# - 일반 백트래킹 알고리즘 -
# 문제: n * n 의 정사각형 안에 n개의 퀸이 자신의 일직선상 및 대각선상에 아무것도 놓이지 않아야함.
def checknode(v):
    pass
     # if promising(v): # v 노드가 유망하다면,
         # if 솔루션이 있으면:
             # 출력
         # else:
             # for u in each child of v:
                 # checknode(v)
