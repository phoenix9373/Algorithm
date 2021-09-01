# 20200807_문제점:
# 1. 검 흰 검 흰 (새로운)검 -> 검 흰 검 검 검 / 검 검 검 검 검()
# 2. 게임이 모두 1, 2로 모두 채워지는 것은 아니다.
import sys
sys.stdin = open('input.txt', 'r')
for tc in range(1, int(input())+1):
    n, m = map(int, input().split())
    arr = [[0]*n for i in range(n)]
    d = [n//2, n//2-1]
    for i in d:
        for j in d:
            if i == j:
                arr[i][j] = 2
            else:
                arr[i][j] = 1
    print(arr)
    # m번 반복. 대각선 추가.
    dx = [0, 0, -1, 1] + [-1, 1, 1, -1]
    dy = [1, -1, 0, 0] + [1, 1, -1, -1]
    for _ in range(m):
        y, x, c = map(int, input().split())
        x -= 1
        y -= 1
        # 현재 위치 (i, j) = (y, x)
        # 상하좌우 탐색. 2칸씩.
        # index 제한 조건 추가.
        # 같은 색깔이면 중간의 1칸을 그 값으로 바꾼다.
        # 상하좌우 모두 바꿔도 ok.
        for k in range(8):
            for z in range(n-1, 1, -1):
                X = x + dx[k]*z
                Y = y + dy[k]*z
                temp = []
                if 0<=X<=(n-1) and 0<=Y<=(n-1):
                    for v in range(1, z):
                        if arr[Y-dy[k]*v][X-dx[k]*v] == 0:
                            temp.append(0)
                    if (0 not in temp) and (arr[Y][X] == c):
                        arr[y][x] = c # 조건을 모두 만족하면 해당 점을 c로 채운다.
                        for v in range(1, z): # 상하좌우 등으로 이동한 값에 c가 있으면, c로 그 사이를 다 채운다.
                            arr[Y-dy[k]*v][X-dx[k]*v] = c
    b, w = 0, 0
    print(arr)
    for row in arr:
        b += row.count(1)
        w += row.count(2)
    print(f'#{tc} {b} {w}')