# 경로압축는 루트 노드를 찾는 효율성을 위해 만들어짐.
# '그래프 연결성' 확인하기에 잘 활용됨
# MST 알고리즘.
# 각 집합에 속한 원소의 수 관리: 가장 큰 집합 추적하기
# 집합의 노드 개수가 몇 개 이상이 되는 시점 찾기.

p = [0] * 100
rank = [0] * 100


def make_set(x):
    p[x] = x
    rank[x] = 0


# 특정 노드에서 루트까지의 경로에 존재하는 노드가 루트를 부모로 가리키도록 갱신
def find_set(x):
    if x != p[x]:  # 자기 자신을 가리키지 않으면 부모를 호출.
        p[x] = find_set(p[x])
    return p[x]


def union(x, y):
    link(find_set(x), find_set(y))


def link(x, y):
    if rank[x] > rank[y]:
        p[y] = x
    else:
        p[x] = y

    if rank[x] == rank[y]:
        rank[y] += 1