def make_set(node):
    tree[node] = node
    rank[node] = 0


def find_set(node):
    if tree[node] != node:
        tree[node] = find_set(tree[node])
    return tree[node]


def union(u, v):
    root1 = find_set(u)
    root2 = find_set(v)

    # union-by-rank 기법
    if rank[root1] > rank[root2]:
        tree[root2] = root1
    else:
        tree[root1] = root2
        if rank[root1] == rank[root2]:
            rank[root2] += 1


def kruskal():
    mst = []

    # 초기화
    for node in range(V + 1):
        make_set(node)

    for edge in edges:
        u, v, w = edge
        if find_set(u) != find_set(v):
            union(u, v)
            mst.append(edge)
    return mst


for tc in range(1, int(input()) + 1):
    V, E = map(int, input().split())
    edges = sorted([list(map(int, input().split())) for _ in range(E)], key=lambda x: x[2])
    tree = dict()
    rank = dict()
    res = kruskal()
    ans = sum(list(zip(*res))[2])
    print('#{} {}'.format(tc, ans))
# 1
# 2 3
# 0 1 1
# 0 2 1
# 1 2 6