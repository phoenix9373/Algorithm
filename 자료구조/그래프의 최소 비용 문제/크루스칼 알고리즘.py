tree = {}
rank = {}


def make_set(node):
    tree[node] = node
    rank[node] = 0


def find_set(node):
    if node != tree[node]:
        tree[node] = find_set(tree[node])
    return tree[node]


def union(u, v):
    root1 = find_set(u)
    root2 = find_set(v)

    if rank[root1] > rank[root2]:
        tree[root2] = root1
    else:
        tree[root1] = root2
        if rank[root2] == rank[root1]:
            rank[root2] += 1 # root1을 root2에 붙였으므로


def kruskal(graph):
    mst = []
    mst_cost = 0

    for i in range(V + 1):
        make_set(i)

    graph = sorted(graph, key=lambda x: x[2])

    for g in graph:
        u, v, w = g
        if find_set(u) != find_set(v):
            union(u, v)
            mst.append(g)
    return mst


for tc in range(1, int(input()) + 1):
    V, E = map(int, input().split())
    lines = sorted([list(map(int, input().split())) for _ in range(E)], key=lambda x: x[2])
    res = sum([i[2] for i in kruskal(lines)])
    print('#{} {}'.format(tc, res))