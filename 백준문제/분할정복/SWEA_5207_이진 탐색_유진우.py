# B에 속한 어떤 수가 A에 있고, 양쪽구간을 번갈아 선택하게 되는 숫자의 개수.
# 이진 탐색 중 m에 해당하는 값이 B에 있으면 cnt += 1
import sys

sys.stdin = open('input.txt', 'r')

for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    A = sorted(list(map(int, input().split())))
    B = sorted(list(map(int, input().split())))
    cnt = 0

    for k in B:
        direction = 0  # right = 1, left = -1
        l, r = 0, len(A) - 1
        while True:
            m = (l + r) // 2
            if len(A):
                if A[m] == k:
                    cnt += 1
                    break
                elif A[m] > k:
                    l, r = l, m - 1
                    if direction == 1:
                        break
                    else:
                        direction = 1
                    continue
                else:
                    l, r = m + 1, r
                    if direction == -1:
                        break
                    else:
                        direction = -1
                    continue
            else:
                break
    print('#{} {}'.format(tc, cnt))
# 5 5
# 1 3 5 7 9
# 1 2 3 4 5


# 1
# 3 3
# 1 2 3
# 2 3 4
