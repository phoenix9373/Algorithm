def preorder(v):
    if tree.get(v) != None:
        print(v, end='')
        preorder(tree[v][0])
        preorder(tree[v][1])


def inorder(v):
    if tree.get(v) != None:
        inorder(tree[v][0])
        print(v, end='')
        inorder(tree[v][1])


def postorder(v):
    if tree.get(v) != None:
        postorder(tree[v][0])
        postorder(tree[v][1])
        print(v, end='')


N = int(input())
tree = {}

for _ in range(N):
    p, lc, rc = input().split()
    tree[p] = [lc, rc]


preorder('A')
print()
inorder('A')
print()
postorder('A')