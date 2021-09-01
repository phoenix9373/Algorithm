# 13
# 1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13

# 입력은 위와같이 받음.

N = int(input())  # 노드 개수 받기

info = list(map(int, input().split()))
tree = [0] * 100  # 노드의 개수보다 크게 설정.

for i in range(0, len(info), 2):
    p = info[i]
    c = info[i + 1]

    # 초기 설정.
    if p not in tree:
        idx = -1
    else:
        idx = tree.index(p)

    # 값 삽입
    if idx == -1:         # 아무것도 없으면 처음 노드에 각각 채우고,
        tree[1] = p
        tree[2] = c
    else:                 # 값이 있으면 부모 노드의 인덱스를 기준으로 좌우 측을 조회.
        if tree[idx * 2] == 0:   # 좌측부터 채운다.
            tree[idx * 2] = c
        else:
            tree[idx * 2 + 1] = c

def preOrder(index):
    print(tree[index], end=' ')
    if tree[index*2] != 0:
        preOrder(index*2)
    if tree[index*2 + 1] != 0:
        preOrder(index*2 + 1)

preOrder(1)