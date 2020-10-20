N = int(input())
info = list(map(int, input().split()))

tree = [[0] * 3 for _ in range(N + 1)] # [좌, 우, 부모]

for i in range(0, len(info), 2):
    p = info[i]
    c = info[i + 1]

    if tree[p][0] == 0:
        tree[p][0] = c
    else:
        tree[p][1] = c

    tree[c][2] = p

def preOreder(index):
    print(index, end=' ')
    if tree[index][0] != 0:
        preOreder(tree[index][0])
    if tree[index][1] != 0:
        preOreder(tree[index][1])

preOreder(1)