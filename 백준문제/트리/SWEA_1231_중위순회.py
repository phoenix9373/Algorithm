for tc in range(1, 11):
    N = int(input())
    tree = [[0] * 3 for _ in range(N + 1)]
    for _ in range(N):
        tmp = input().split()
        if len(tmp) == 4:
            tree[int(tmp[0])][0] = tmp[1]
            tree[int(tmp[0])][1] = int(tmp[2])
            tree[int(tmp[0])][2] = int(tmp[3])
        elif len(tmp) == 3:
            tree[int(tmp[0])][0] = tmp[1]
            tree[int(tmp[0])][1] = int(tmp[2])
        else:
            tree[int(tmp[0])][0] = tmp[1]

    def inorder(node):
        if tree[node][0]:
            inorder(tree[node][1])
            print(tree[node][0], end='')
            inorder(tree[node][2])

    print('#{} '.format(tc), end='')
    inorder(1)
    print()