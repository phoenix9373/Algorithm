def operation(idx):
    t = str(tree[idx][1])
    if t in '-+*/':
        l = tree[idx][2]
        r = tree[idx][3]
        l_v = tree[l][1]
        r_v = tree[r][1]
        if t == '+':
            tree[idx][1] = l_v + r_v
        elif t == '-':
            tree[idx][1] = l_v - r_v
        elif t == '*':
            tree[idx][1] = l_v * r_v
        elif t == '/':
            tree[idx][1] = l_v / r_v


for tc in range(1, 11):
    N = int(input())
    tree = [[0] * 4 for _ in range(N + 1)]

    for i in range(1, N + 1):
        tmp = list(input().split())
        for j in range(len(tmp)):
            if tmp[j].isdigit():
                tree[i][j] = int(tmp[j])
            else:
                tree[i][j] = tmp[j]

    for i in range(N, 0, -1):
        operation(i)

    print('#{} {}'.format(tc, int(tree[1][1])))