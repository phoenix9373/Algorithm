# input 파일을 가져와서 실행.
# import sys
# sys.stdin = open('input.txt', 'r')

# 1. 함수 정의
def test(x, y, m, d, k):  # x, y는 기준점. m, d는 시작값과 등차. k는 n번째 기준점을 나타내는 값.
    arr[x][y] = m + d * k  # 기준점을 먼저 채움.
    repeat = 2 * k  # 각 행, 열당 반복 횟수.
    dy = [1, 0, -1, 0] # 좌우 이동
    dx = [0, 1, 0, -1] # 상하 이동

    for i in range(4):  # 우, 하, 좌, 상 순서.
        for _ in range(1, repeat + 1):  # repeat = 3이면 2번 반복.
            nx = x + dx[i] # 좌우 이동 갱신
            ny = y + dy[i] # 상하 이동 갱신
            arr[nx][ny] = m + d * k # 시작값 m에 등차 d를 k번 곱한 값을 넣는다.
            x, y = nx, ny # 이동한 위치를 다시 기준점으로.

# 2. 실행 구문
for tc in range(1, int(input())+1): # 테스트 케이스만큼 반복
    N, M, D = map(int, input().split()) # split()으로 나누어 int로 각각 N, M, D 저장.

    arr = [[0] * N for _ in range(N)] # 빈 2차원 배열 생성.
    total_rep = N // 2 + 1 # 총 반복 횟수
    f_x = N // 2 # row의 start index
    f_y = N // 2 # col의 start index
    K = 0 # 등차를 k번 곱함.

    for _ in range(total_rep): # 총 반복 횟수, n=7이면 좌측 위 대각선으로 4번 올라가면 된다.
        test(f_x, f_y, M, D, K) # 함수 호출.
        f_x -= 1 # row를 위로
        f_y -= 1 # col을 왼쪽으로
        K += 1 # 등차를 +1 만큼 더 곱해준다.

    row_sum = [sum(row) for row in arr] # arr에 있는 row를 가져와서 sum하여 저장.
    print('#{}'.format(tc), end=' ') # tc print
    print(*row_sum) # 각 행의 합 출력.