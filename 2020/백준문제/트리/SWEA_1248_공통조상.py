def parent(a):
    a_parent = []

    while True:
        if tree[a][2] != 0:
            a_parent.append(tree[a][2])
            a = tree[a][2] # 부모 노드 초기화.
        else:
            break
    return a_parent


def counting(node):
    global cnt
    if node:
        cnt += 1
        counting(tree[node][0]) # 왼쪽.
        counting(tree[node][1]) # 오른쪽.


for tc in range(1, int(input()) + 1):
    V, E, A, B = map(int, input().split())
    tree = [[0] * 3 for _ in range(V + 1)]
    info = list(map(int, input().split()))
    for i in range(E):
        p, c = info[i*2], info[i*2 + 1]
        if tree[p][0] == 0:
            tree[p][0] = c
        else:
            tree[p][1] = c
        tree[c][2] = p

    candi_a = parent(A)
    candi_b = parent(B)
    tmp = 0
    for i in range(len(candi_a)):
        for j in range(len(candi_b)):
            if candi_a[i] == candi_b[j]:
                tmp = candi_a[i]
                break
        if tmp:
            break

    cnt = 0
    counting(tmp)

    print('#{} {} {}'.format(tc, tmp, cnt))