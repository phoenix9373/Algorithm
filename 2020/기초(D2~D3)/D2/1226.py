# stack 개념을 활용하자.
# 방향이 전환되는 부분의 점을 q에 저장.
# 막힌 부분에서 어떻게 나올까?
# 현재의 방향이 이전의 방향과 다르면 먼저 

for _ in range(10):
    c = int(input())
    arr = [list(map(int, ' '.join(input()).split())) for _ in range(16)]
    p = 0
    q = []
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    q.append([1, 1])
    while q:
        [x, y] = q.pop() # 가장 마지막 요소를 반환 후 삭제.
        
        for k in range(4):
            xx = x + dx[k]
            yy = y + dy[k]
            if (arr[xx][yy] == 0) or (arr[xx][yy] == 2):
                q.append([xx, yy])
            if arr[xx][yy] == 3:
                p = 1
        arr[x][y] = 1
    print(f'#{c} {p}')