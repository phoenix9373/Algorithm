# input 파일을 가져와서 실행.
# import sys
# sys.stdin = open('input.txt', 'r')

def dfs(v):
    x, y = v[0], v[1] # 시작점을 각각 x, y로 받는다. x는 세로(N), y는 가로(M)
    visited[x][y] = 1 # 방문 표시를 한다.

    # 상하좌우 이동
    dx = [0, 0, 1, -1] 
    dy = [1, -1, 0, 0]
    
    # 1. 해당 좌표에서 상하좌우를 탐색한다.
    # 2. index 범위 조건 + 방문 여부 + 연못 여부 를 따져서 다음 좌표를 탐색한다.
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] == 0 and arr[nx][ny] == 1:
            dfs([nx, ny]) # 모든 좌표를 탐색했으면 자동으로 끝난다.


for tc in range(1, int(input()) + 1):
    M, N, K = map(int, input().split()) # M은 가로, N은 세로, K는 연못 좌표.
    arr = [[0] * M for _ in range(N)] # col의 길이 = 가로 = M /// row의 길이 = 세로 = N, 빈 arr 생성.
    visited = [[0] * M for _ in range(N)] # 방문 여부를 체크할 빈 2차원 배열 생성.

    # 연못 좌표 1로 채우기.
    for _ in range(K):
        y, x = map(int, input().split()) # y는 col, x는 row
        arr[x][y] = 1 # 연못 좌표에 1을 채운다.

    cnt = 0 # 잉어의 개수 세기.
    
    # 모든 좌표에 대해 1번씩 실행.
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1 and visited[i][j] == 0: # 모든 좌표 중 1이고, 방문하지 않은 곳에 대해 dfs 실행.
                dfs([i, j]) # 조건에 맞는 좌표에서 함수 호출.
                cnt += 1 # dfs가 실행되면 잉어가 한 마리 추가됨.
                
    print('#{} {}'.format(tc, cnt))