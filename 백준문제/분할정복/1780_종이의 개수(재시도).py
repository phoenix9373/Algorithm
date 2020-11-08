import sys
from operator import add
ans = [0] * 3
data = []
temp = 0

n = int(input())
for i in range(n):
    data.append([int(i) for i in sys.stdin.readline().rstrip().split()])


def lastpaper(x, y, size):
    global ans
    tmpans = [0, 0, 0]
    init = data[x][y]
    sameflag = True
    for i in range(size):
        for j in range(size):
            if data[x + i][y + j] != init:
                sameflag = False
                break
        if sameflag == False:
            break
    return sameflag, init


def numpaper(size, x, y):
    global ans

    gflag, i = lastpaper(x, y, size)
    if gflag:
        ans[i + 1] += 1
    else:
        for i in range(3):
            for j in range(3):

                numpaper(size//3, x + i*(size//3), y + j*(size//3))

numpaper(n, 0, 0)
print("{}\n{}\n{}".format(ans[0],ans[1],ans[2]))