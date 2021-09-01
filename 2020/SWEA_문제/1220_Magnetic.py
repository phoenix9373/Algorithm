# 1 다음에 2가 나오는 것.
# col 기준으로 탐색
import sys
sys.stdin = open('input.txt', 'r')
for tc in range(1, 11):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    arr_T = [list(col) for col in zip(*arr)]
    count = 0
    for i in range(n):
        tmp = []
        for j in range(n):
            if arr_T[i][j] != 0:
                tmp.append(arr_T[i][j])
        for k in range(len(tmp) - 1):
            if tmp[k] == 1 and tmp[k + 1] == 2:
                count += 1
    print('#{} {}'.format(tc, count))