for tc in range(1, 11):
    V, E = map(int, input().split())

    edges = list(map(int, input().split()))

    prev_arr = [[0] * (V + 1) for _ in range(V + 1)]

    order = []  # 작업순서를 담음.

    work = [0] * (V + 1)  # 작업한 노드에 대해 기록

    for i in range(0, len(edges), 2):
        st, ed = edges[i], edges[i + 1]
        prev_arr[ed][st] = 1

    # 선행 작업이 하나도 없는 일은 미리 담아두자.
    # 시작 노드들.
    for i in range(1, len(prev_arr)):
        if prev_arr[i].count(1) == 0:
            order.append(i)
            work[i] = 1

    while len(order) != V:  # order에 총 V개를 담을 때까지 반복.
        for i in range(1, V + 1): # 전체 작업 확인.
            if work[i] == 0:      # 작업 안한 경우,
                for j in range(1, V + 1):
                    if prev_arr[i][j] == 1: # i를 위한 선행작업 j가 있는데
                        if work[j] == 0: # 만약 선행작업을 하지 않았다면,
                            break # 멈춘다.
                else: # 선행작업을 모두 해서 for문을 통과
                    order.append(i) # 하면 작업에 추가한다.
                    work[i] = 1 # 그리고 작업 표시를 한다.


