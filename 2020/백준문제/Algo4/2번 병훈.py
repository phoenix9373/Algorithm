def cross_stones(cur,visited,count):
    global MAX
    # 밟은 돌이 M보다 크면 안된다
    if count > M:return
    # 현재 인덱스가 N-1 이면 모든 돌을 거쳐왔다.
    # 조건에 맞는지 확인
    if cur == N-1:
        # 돌을 밟은 수가 M과 같아야한다.
        if count == M:
            sumation = 0
            # 밟은 돌의 index를 알아야 점수를 더한다.
            for i in range(len(visited)):
                if visited[i]:
                    sumation += stones[i]
            # 다 더한 점수가 MAX보다 크면 갱신
            if MAX < sumation:
                MAX = sumation
    else:
        # 전에 돌을 뛰어넘었으면 이번 돌은 무조건 밟아야한다
        if visited[-1] == False:
            cross_stones(cur+1,visited+[True],count+1)
        # 전에 돌을 밟았으면 이번 돌은 밟거나 뛰어 넘거나
        else:
            cross_stones(cur+1,visited+[True],count+1)
            cross_stones(cur+1,visited+[False],count)

for t in range(1,int(input())+1):
    N,M = map(int,input().split())
    stones = list(map(int,input().split()))
    MAX = 0
    cross_stones(0,[True],1) # 현재위치, 밟았는지 여부, ?
    cross_stones(0,[False],0)
    print("#{} {}".format(t,MAX))


# 4
# 7 5
# 5 4 2 7 1 2 3
# 8 6
# 10 10 1 3 1 5 4 7
# 3 1
# 1 3 1