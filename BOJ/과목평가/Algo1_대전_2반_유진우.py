# N * M
# 한 변의 길이 K인 사각 테두리의 숫자 합계 중 최대값과 최솟값의 차.
# (N - K + 1) * (M - K + 1) 개 존재.

# 1. 좌표 변경.
di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]


# 2. 테두리 합 구하는 함수.
def get_sum(x, y, k):
    tmp_sum = 0  # 임시로 활용할 sum 변수 설정 후,

    for t in range(4):  # 하 -> 우 -> 상 -> 좌 방향으로 움직임.
        for _ in range(k - 1):  # 각각의 이동마다 K - 1번 이동.
            nx = x + di[t]  # row 방향 이동.
            ny = y + dj[t]  # col 방향 이동.
            tmp_sum += arr[nx][ny]  # 이동한 시점에서 sum 변수에 값을 더함.
            x, y = nx, ny  # 이동한 곳으로 x, y 값 초기화
    return tmp_sum


# 3. 실행 구문
for tc in range(1, int(input()) + 1):
    N, M, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]  # N * M 배열
    maxA = 0
    minA = pow(2, 30)

    # 시작점 배열을 생성.
    # row는 index가 0부터 (N - K).
    # col은 index가 0부터 (M - K).
    for i in range(N - K + 1):
        for j in range(M - K + 1):
            tmp = get_sum(i, j, K)  # 위 함수로 테두리의 sum 값 반환.
            if tmp >= maxA:  # 최댓값 초기화.
                maxA = tmp
            if tmp <= minA:  # 최솟값 초기화.
                minA = tmp

    rep = maxA - minA  # 최댓값과 최솟값의 차이.
    print('#{} {}'.format(tc, rep))