'''
13
1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13
'''
def preorder(node):
    global cnt
    if node:
        print(node, end=' ')
        cnt += 1
        preorder(tree[node][0])  # 좌
        preorder(tree[node][1])  # 우


V = int(input()) # 정점 개수
E = V - 1        # 간선 개수

tree = [[0] * 3 for _ in range(V + 1)] # [좌, 우, 부모]
tmp = list(map(int, input().split()))  # 입력
cnt = 0

# 인접 리스트 tree 저장.
for i in range(E):
    p, c = tmp[i*2], tmp[i*2 + 1]
    if tree[p][0] == 0:   # 부모 노드 p의 왼쪽 자식이 비었으면,
        tree[p][0] = c    # left
    else:                 # 오른쪽 자식이 비었으면.
        tree[p][1] = c    # right

    tree[c][2] = p        # parent

print(tree)
preorder(1)
print()
print(cnt)