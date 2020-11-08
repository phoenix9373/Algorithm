def find_set(node):
    while node != tree[node]:
        node = tree[node]
    return node


def union(u, v):
    r1 = find_set(u)
    r2 = find_set(v)

    if rank[r1] > rank[r2]:
        tree[r2] = r1
    else:
        tree[r1] = r2
        if rank[r1] == rank[r2]:
            rank[r2] += 1


for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    tree = {}
    rank = {}
    info = list(map(int, input().split()))

    for i in range(1, N + 1):
        tree[i] = i
        rank[i] = 0

    for j in range(M):
        s, e = info[j*2], info[j*2 + 1]
        union(s, e)

    ans = set()
    for val in tree.values():
        ans.add(val)
    print('#{} {}'.format(tc, len(ans)))