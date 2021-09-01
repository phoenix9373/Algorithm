def preorder(node):
    if node: # 0만 아니면..!?
        print(node, end=' ')
        preorder(tree[node][0]) # 왼쪽 노드
        preorder(tree[node][1]) # 오른쪽 노드



# 하나의 노드에 대해 [좌, 우, 부모] 노드 순으로 저장하자.

V = int(input())
E = V - 1

# tree 구조 생성.
tree = [[0] * 3 for _ in range(V + 1)] # [좌, 우, 부모]
tmp = list(map(int, input().split()))
cnt = 0 # ?

for i in range(E):
    p, c = tmp[i*2], tmp[i*2 + 1]
    if tree[p][0] == 0:
        tree[p][0] = c
    else:
        tree[p][1] = c
    
    tree[c][2] = p # 부모 노드 값 할당.

preorder(1)