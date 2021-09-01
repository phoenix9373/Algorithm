def solution(old):
    # 1. 길이와 새로운 배열을 만든다.
    l = len(old)
    new = [[0] * l for _ in range(l)]

    # 2. 배열의 각각 row, col의 start와 last index를 기록하는 변수를 만든다.
    c_s, c_l = 0, l - 1
    r_s, r_l = 0, l - 1

    # 3. N이 홀수인 경우, 중앙은 움직이지 않으므로 그대로 입력한다.
    if l % 2:
        new[l//2][l//2] = old[l//2][l//2]

    # 4. 각각 c_s와 c_l, r_s와 r_l이 만나기 직전까지 반복을 수행한다.
    while c_s < c_l and r_s < r_l:
        # 5. 각 시도마다 길이를 저장해준다.
        length = c_l - c_s + 1

        # 6. 각 길이만큼 반복해서 시계방향으로 값을 채운다.
        for k in range(length):
            new[r_s][c_s + k] = old[r_l - k][c_s]
        for k in range(length):
            new[r_s + k][c_l] = old[r_s][c_s + k]
        for k in range(length):
            new[r_l][c_l - k] = old[r_s + k][c_l]
        for k in range(length):
            new[r_l - k][c_s] = old[r_l][c_l - k]

        # 7. 바깥쪽을 다 채웠으면 안쪽을 채우기 위해 값을 변경한다.
        c_s += 1
        r_s += 1
        c_l -= 1
        r_l -= 1

    return new


for tc in range(1, int(input()) + 1):
    N, C, X, Y, K, R = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 1. 영역을 벗어나는 경우 -1을 출력하고 다음 케이스로 간다.
    if X + K - 1 > N or Y + K - 1 > N:
        print('#{} {}'.format(tc, -1))
        continue

    # 2. X, Y에서 시작하는 부분 arr를 subarr에 입력한다.
    subarr = [[0] * K for _ in range(K)]
    for idx, i in enumerate(range(Y - 1, Y - 1 + K)):
        for jdx, j in enumerate(range(X - 1, X - 1 + K)):
            subarr[idx][jdx] = arr[i][j]

    # 3. 회전 수를 구한 뒤, subarr에 반복적으로 적용해서 최종 subarr를 얻는다.
    rotation_count = (C % 360) // 90
    for _ in range(rotation_count):
        subarr = solution(subarr)

    # 4. 2번 작업에서 행한 반대 순서로 기존의 arr에 subarr를 삽입한다.
    for idx, i in enumerate(range(Y - 1, Y - 1 + K)):
        for jdx, j in enumerate(range(X - 1, X - 1 + K)):
            arr[i][j] = subarr[idx][jdx]

    print('#{} {}'.format(tc, sum(arr[R - 1])))