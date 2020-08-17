dx=[0, 1, 0, -1]
dy=[1, 0, -1, 0]

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr= [list(map(int, input().split())) for i in range(N)]
    MAX=0 # 가장 많은 이동가능 숫자 개수.
    num=0 # 해당 숫자.
    q = [] # stack

    for i in range(N):
        for j in range(N):
            q.append([i, j]) # 현재 위치의 좌표를 추가.
            cnt = 1

            # Idea: 해당 위치값을 q에 추가하는 방법.
            # 1. 리스트 q에 이동가능한 좌표점이 있으면 
            #    q가 빌때까지 하나씩 좌표점을 꺼내어 반복하여 탐색.
            while q: # -------- Stack 개념.
                [x, y] = q.pop() # 2. q에서 하나 꺼냄.
                for k in range(4): # 3. 4개 방향으로 탐색 반복.
                    xx = x+dx[k]
                    yy = y+dy[k]

                    if 0<=xx<N and 0<=yy<N: # 4. indexError 방지를 위한 조건.
                        if arr[xx][yy]==arr[x][y]+1: # 5. 문제 조건. 현재 위치값은 다음 위치값보다 1 작다.
                            cnt+=1
                            q.append([xx,yy]) # 6. 조건에 맞으면 옮긴 위치를 q에 추가하여 다시 현재 위치로 활용한다.

            if MAX==cnt and arr[i][j]<num: # 7. MAX값 갱신 전, 이전 숫자와 현재 숫자를 비교하여 같으면 더 작은 숫자로 할당.
                num = arr[i][j]

            if MAX<cnt: # 8. MAX 값 갱신 및 num 갱신.
                MAX=cnt
                num = arr[i][j]

    print('#{} {} {}'.format(tc, num, MAX))