dx = [0, 0, -1, 1] + [1, 1, -1, -1] # 상하좌우 우우좌좌
dy = [1, -1, 0, 0] + [1, -1, 1, -1] # 상하좌우 상하상하

def check(x, y, c):
    o = 1 if c == 2 else 2 # 1이면 2, 2이면 1
    for k in range(8): # 8방향 탐색.
        nx = x + dx[k]
        ny = y + dy[k]
        cnt = 0
        while (0 <= nx < n) and (0 <= ny < n) and arr[nx][ny] != 0:
                if arr[nx][ny] == o: # 다른 색일 때, cnt + 1.
                    cnt += 1
                if arr[nx][ny] == c: # 같은 색일 때, cnt 만큼 (x,y)에서 같은 방향으로 cnt만큼 이동할때마다 색깔 바꿈.
                    for t in range(1, cnt+1):
                        arr[x+t*dx[k]][y+t*dy[k]] = c
                    break # 같은 색을 만나면 사이의 색깔을 바꾸고 종료.
                nx += dx[k] # 같은 방향으로 한 번 더 탐색.
                ny += dy[k]


for tc in range(1, int(input())+1):
    n, m = map(int, input().split())
    arr = [[0] * n for _ in range(n)]

    # 초기 설정.
    for i in range(n//2 - 1, n//2 + 1):
        for j in range(n//2 - 1, n//2 + 1):
            if i == j:
                arr[i][j] = 2
            else:
                arr[i][j] = 1
    # 함수 실행.
    for _ in range(m):
        ix, iy, ic = map(int, input().split())
        arr[ix-1][iy-1] = ic
        check(ix-1, iy-1, ic) # index를 맞추기 위해 -1

    # 블랙, 화이트 개수 세기
    b = 0
    w = 0

    for i in range(n):
        for j in range(n):
            if arr[i][j] == 2:
                w += 1
            if arr[i][j] == 1:
                b += 1
    print('#{} {} {}'.format(tc, b, w))
