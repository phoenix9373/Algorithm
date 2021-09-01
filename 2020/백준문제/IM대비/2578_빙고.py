import sys
from itertools import chain


def check():
    cnt = 0

    for i in range(5):
        # 가로
        if sum(bingo[i * 5: (i + 1) * 5]) == -5:
            cnt += 1
        # 세로
        if sum(bingo[i::5]) == -5:
            cnt += 1

    # 대각선
    if sum(bingo[0::6]) == -5:
        cnt += 1
    if sum(bingo[4:21:4]) == -5:
        cnt += 1
    return cnt


bingo = list(chain(*[list(map(int, sys.stdin.readline().split())) for _ in range(5)]))
nums = list(chain(*[list(map(int, sys.stdin.readline().split())) for _ in range(5)]))

for c, i in enumerate(nums):
    idx = bingo.index(i)
    bingo[idx] = -1
    if c >= 11:
        tmp = check()
        if tmp >= 3:
            print(c + 1)
            break