# 12
# 1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13

V = int(input())
info = list(map(int, input().split()))
tree = [[0, 0] for _ in range(100)]

for i in range(0, len(info), 2):
    p, c = info[i], info[i + 1]

    if tree[p][0] == 0:
        tree[p][0] = c
    else:
        tree[p][1] = c


def preorder(idx):
    if idx:
        print(idx, end=' ')
        preorder(tree[idx][0]) # 좌
        preorder(tree[idx][1]) # 우


def inorder(idx):
    if idx:
        preorder(tree[idx][0]) # 좌
        print(idx, end=' ')
        preorder(tree[idx][1]) # 우


def postorder(idx):
    if idx:
        preorder(tree[idx][0]) # 좌
        preorder(tree[idx][1]) # 우
        print(idx, end=' ')


preorder(1)
print()
inorder(1)
print()
postorder(1)