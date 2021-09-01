def push(node):

    if node <= N:
        if tree[node] == 0:
            tree[node] = push(node*2) + push(node*2 + 1)
            return tree[node]
            # if node != 1:
            #     return tree[node]
        else:
            return tree[node]
    return 0


for tc in range(1, int(input()) + 1):
    N, M, L = map(int, input().split())
    tree = [0 for _ in range(N + 1)] # [값]

    for _ in range(M):
        leaf, value = map(int, input().split())
        tree[leaf] = value

    push(1)
    print('#{} {}'.format(tc, tree[L]))