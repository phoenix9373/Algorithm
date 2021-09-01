# 13
# 1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13

N = int(input())
info = list(map(int, input().split()))
tree = [0] * 100

# 1차원 배열 이용.
for i in range(0, len(info), 2):
    p = info[i]
    c = info[i + 1]

    if p not in tree:
        idx = -1
    else:
        idx = tree.index(p)
    # 1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13
    if idx == -1:
        tree[1] = p
        tree[2] = c
    else:
        # 왼쪽 자식이 비었으면 거기
        if tree[idx*2] == 0:
            tree[idx*2] = c
        # 아니라면 오른쪽
        else:
            tree[idx*2 + 1] = c

def preOrder(index):
    print(tree[index], end=' ')
    if tree[index*2] != 0:
        preOrder(index*2)
    if tree[index*2 + 1] != 0:
        preOrder(index*2 + 1)

def inOrder(index):
    if tree[index*2] != 0:
        inOrder(index*2)
    print(tree[index], end=' ')
    if tree[index*2 + 1] != 0:
        inOrder(index*2 + 1)

def postOrder(index):
    if tree[index*2] != 0:
        postOrder(index*2)
    if tree[index*2 + 1] != 0:
        postOrder(index*2 + 1)
    print(tree[index], end=' ')

postOrder(1)