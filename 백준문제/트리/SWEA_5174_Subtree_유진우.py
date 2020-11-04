# 전위 탐색
def preorder(node):
    global cnt
    if node: # node 값이 0이 아니면
        cnt += 1
        preorder(tree[node][0]) # 왼쪽
        preorder(tree[node][1]) # 오른쪽

for tc in range(1, int(input()) + 1):
    E, X = map(int, input().split()) # X는 기준이 될 노드 번호.
    N = E + 1
    info = list(map(int, input().split()))
    tree = [[0] * 2 for _ in range(N + 1)]
    cnt = 0

    for i in range(E):
        p, c = info[i*2], info[i*2 + 1]
        if tree[p][0] == 0:
            tree[p][0] = c # 왼쪽
        else:
            tree[p][1] = c # 오른쪽 자식 노드

    preorder(X)
    print('#{} {}'.format(tc, cnt))
