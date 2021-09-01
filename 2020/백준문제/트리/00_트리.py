import sys

sys.stdin = open('input_00.txt', 'r')


def preorder(n):
    if n: # 트리가 존재하면, 0이 아니면.
        print(n, end=' ')
        preorder(tree[n][0])
        preorder(tree[n][1])


def inorder(n):
    if n: # 트리가 존재하면, 0이 아니면.
        preorder(tree[n][0])
        print(n, end=' ')
        preorder(tree[n][1])


def postorder(n):
    if n: # 트리가 존재하면, 0이 아니면.
        preorder(tree[n][0])
        preorder(tree[n][1])
        print(n, end=' ')


# 트리 입력받기.
N = int(input())  # 노드의 수.
E = 12  # 간선의 수.
tree = [[0, 0, 0] for _ in range(N + 1)]
arr = list(map(int, input().split()))

for i in range(E):
    if tree[arr[2 * i]][0] == 0:
        tree[arr[2 * i]][0] = arr[2 * i + 1]
    else:
        tree[arr[2 * i]][1] = arr[2 * i + 1]

    tree[arr[2 * i + 1]][2] = arr[2 * i]

print(arr)
preorder(1)
print()
inorder(1)
print()
postorder(1)
