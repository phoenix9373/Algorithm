def heappush(value):
    global count
    count += 1 # tree의 index를 호출 될 때마다 늘린다.
    heap[count] = value

    cur = count
    parent = count // 2

    while parent and heap[parent] > heap[cur]:
        heap[parent], heap[cur] = heap[cur], heap[parent]
        cur = parent # 현재보다 위로 올라가서 다시 수행.
        parent = cur // 2



for tc in range(1, int(input()) + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    heap = [0] * (N + 1)
    count = 0

    for i in range(N):
        heappush(arr[i])

    ret = 0
    while N != 0:
        N = N // 2
        if N == 0:
            break
        ret += heap[N]

    print('#{} {}'.format(tc, ret))