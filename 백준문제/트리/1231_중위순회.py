import sys
sys.stdin = open('input.txt', 'r')

def inorder_travers(T): # T == tree[1]
    if T: # None이 아니면. 자식 노드가 없는 경우, 0을 반환하고 None으로 이어짐.
        inorder_travers(tree[T[2]])
        visited.append(T[1])
        inorder_travers(tree[T[3]])

for tc in range(1, 11):
    N = int(input())
    tree = [[0] * 4 if k != 0 else [] for k in range(N + 1)]
    visited = []

    for i in range(1, N + 1):
        info = input().split()
        for j, src in enumerate(info):
            tree[i][j] = int(src) if src.isdigit() else src
    inorder_travers(tree[1])
    print('#{}'.format(tc), end=' ')
    print(*visited, sep='')