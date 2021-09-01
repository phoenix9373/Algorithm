def treepush(node):
    global treecount

    if node <= N and tree[node] == 0: # 해당 노드가 0이면 수행.
        treepush(node*2) # 왼쪽 자식 노드.
        if tree[node] == 0:
            treecount += 1 # 입력하기 직전에 +1을 하고, 입력한다.
            tree[node] = treecount
        treepush(node*2 + 1) # 오른쪽 자식 노드.
        if node != 1:
            treepush(node//2) # 부모 노드.


for tc in range(1, int(input()) + 1):
    N = int(input())
    tree = [0] * (N + 1)
    treecount = 0

    first_node = 1
    while first_node <= N:
        first_node *= 2
    first_node = int(first_node / 2)
    treepush(first_node)
    print('#{} {} {}'.format(tc, tree[1], tree[N//2]))