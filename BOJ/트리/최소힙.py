def heappush(value):
    global heapcount
    heapcount += 1
    heap[heapcount] = value
    cur = heapcount
    parent = cur // 2 # 부모노드의 번호

    # 루트가 아니고, if 부모노드값 > 자식노드값 = > swaq (최소힙)
    while parent and heap[parent] > heap[cur]: # 값이 0이 아닐때
        heap[parent], heap[cur] = heap[cur], heap[parent]
        cur = parent       # index 업데이트
        parent = cur // 2  # index 업데이트


def heappop():
    global heapcount
    retValue = heap[1]           # 1. 루트 노드를 복사해둔다.
    heap[1] = heap[heapcount]    # 2. 루트 노드를 지우고, 가장 마지막 노드 번호에 있는 값을 넣는다.
    heap[heapcount] = 0          # 3. 마지막 노드 번호의 값을 0으로 초기화한다.(지운다.)
    heapcount -= 1               # 4. 하나 줄여서 왼쪽으로 간다. 왼쪽이 없으면 바로 위 최우측으로 간다.(index 상으로는 -1 계속)

    parent = 1                   # 루트
    child = parent * 2           # 왼쪽 자식.

    if child + 1 <= heapcount:   # 오른쪽 자식 존재
        if heap[child] > heap[child + 1]:
            child = child + 1
    # 자식노드가 존재하고, 부모노드 > 자식노드 이면 => Swap
    while child <= heapcount and heap[parent] > heap[child]:
        heap[parent], heap[child] = heap[child], heap[parent]
        parent = child
        child = parent * 2
        if child + 1 <= heapcount:  # 오른쪽 자식 존재
            if heap[child] > heap[child + 1]:
                child = child + 1

    return retValue

# 최소힙
# 힙을 1차원으로 구현

heapcount = 0 # 현재 노드 번호. 1, 2, 3, ..., N
temp = [7, 2, 5, 3, 4, 6] # 하나씩 빼서 힙에 집어 넣음
N = len(temp)
heap = [0] * (N + 1) # 인덱스 포함.

for i in range(N):
    heappush(temp[i])

# 삭제 연산
for i in range(N):
    print(heappop(), end=' ')
print()