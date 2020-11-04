# 최소힙 구현

# 삽입
def heappush(value):
    global heapcount
    heapcount += 1 # 먼저 heap의 공간에 heapcount에 해당하는 index 위치에 값을 넣기 위함.
    heap[heapcount] = value # 복사.
    cur = heapcount # 현재 index 값. 즉 heapcount에 해당하는 노드 번호.
    parent = cur // 2 # 좌, 우 모두 마찬가지.

    while parent and heap[cur] < heap[parent]:
        heap[cur], heap[parent] = heap[parent], heap[cur]  # 부모가 있고, 최소힙에서 자식이 부모보다 작으면 바꾼다.
        # 값을 바꾼 뒤, 바꾼 값 위치에서 다시 이 과정을 수행한다.
        cur = parent
        parent = cur // 2 # 언제까지? -> 현재 삽입할 위치에서 1. 부모가 자신보다 값이 작으면 끝, 2. 부모노드가 없는 경우 끝.(루트 노드)


# 삭제
def heappop():
    global heapcount # push를 한 횟수.
    retValue = heap[1]
    heap[1] = heap[heapcount] # 루트 노드를 지우고, 가장 마지막 요소를 넣는다.
    heap[heapcount] = 0       # 루트 노드에 넣은 마지막 요소의 위치에 0으로 초기화 한다.(제거)
    heapcount -= 1            # 가장 마지막 요소의 위치가 한 칸 줄어들었으므로 수정한다.

    # 비교 작업. 일단 왼쪽 자식부터 비교.
    parent = 1                # 현재 parent
    child = parent * 2        # 현재 부모 노드의 왼쪽 자식 노드
                              # 현재 parent가 루트이니, 최소 하나의 노드는 존재함. 그렇다면 왼쪽 자식은 일단 반드시 있음.

    # 오른쪽도 있다면? 자식들끼리 비교해서 최후의 child를 뽑는다.
    if child + 1 <= heapcount:# 근데 오른쪽 자식 노드도 존재할 수 있음.
        if heap[child] > heap[child + 1]: # 게다가 최소힙인데 왼쪽 노드가 오른쪽보다 크다면? 왼쪽은 볼 필요 없음.
            child = child + 1 # 그래서 오른쪽 자식 노드와 부모 노드를 비교하기 위해 갱신해줌.

    # 이제 계속 비교할거야.
    # 자식 노드가 있고, 부모노드 > 자식노드 이면 최소힙이니까 부모가 더 작게끔 바꾸자.
    while child <= heapcount and heap[child] < heap[parent]:
        heap[child], heap[parent] = heap[parent], heap[child]
        # 바꿨으면 더 아래 자식들과도 비교해야지.
        # 현재의 자식을 부모로 지정.
        parent = child
        child = parent * 2
        # 여기서도 똑같이. 왼쪽과 오른쪽 자식 노드부터 비교.
        if child + 1 <= heapcount:
            if heap[child] > heap[child + 1]:
                child = child + 1
    # ---- 여기까지 했으면 루트 노드 삭제하고 맨 마지막 요소 끌어온 걸로 비교 다 하고 자기 자리 찾아갔음.
    # 이건 오름차순이 된다.

    return retValue


heapcount = 0 # 힙의 인덱스를 하나씩 증가시키면서 값 삽입.
temp = [7, 2, 5, 3, 4, 6]
N = len(temp)
heap = [0] * (N + 1) # 자료를 넣을 heap 공간.

for i in range(N): # temp의 개수만큼 반복하여 heap에 원소를 넣음
    heappush(temp[i]) # 순서대로 넣으면서 비교한 후, 자리 바꿈.

print(heap)
# 현재 heapcount는 6이다. 6번의 push 작업을 했음.
for i in range(N):
    print(heappop(), end=' ')