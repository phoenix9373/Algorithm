# import sys
#
# sys.stdin = open('input.txt', 'r')

scores = [0, [0, 1], [0, 2], [0, 4], [0, 8]]


# N극: 0, S극: 1
# 시계: 1, 반시계: -1
def rotation(mag_num, direction, visit):
    visit[mag_num] = 1

    # mag_num번째 자석 옆에 있는 값들 조정.
    for w in adj_list[mag_num]:
        # 이미 방문했으면 무시.
        if visit[w] == 1:
            continue
        if w > mag_num:
            if info[mag_num][(idx[mag_num] + 2) % 8] != info[w][(idx[w] + 6) % 8]:
                rotation(w, -direction, visit)  # 다를 경우, 반대 방향.
        if w < mag_num:
            if info[mag_num][(idx[mag_num] + 6) % 8] != info[w][(idx[w] + 2) % 8]:
                rotation(w, -direction, visit)  # 다를 경우, 반대 방향.

    # 화살표 갱신.
    if direction == 1:
        idx[mag_num] = 7 if idx[mag_num] == 0 else idx[mag_num] - 1
    else:
        idx[mag_num] = (idx[mag_num] + 1) % 8


T = int(input())
for tc in range(1, T + 1):
    K = int(input())
    info = [[0]] + [list(map(int, input().split())) for _ in range(4)]  # 자석 정보
    arr = [list(map(int, input().split())) for _ in range(K)]  # [mag_num, direc]

    adj_list = [0, [2], [1, 3], [2, 4], [3]]
    idx = [0] * 5

    # 회전 시작.
    for case in arr:
        visited = [0] * 5
        mag, drc = case
        rotation(mag, drc, visited)

    res = 0
    for k in range(1, 5):
        tmp = idx[k]  # 화살표의 index
        magnetic = info[k][tmp]  # 1이면 N, 0이면 S. 화살표가 가리키는 자석.
        res += scores[k][magnetic]  # 자석에 따른 값.

    print('#{} {}'.format(tc, res))