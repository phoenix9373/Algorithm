di = [0, 0, -1, 1]
dj = [1, -1, 0, 0]

def find(v, ans):

    if len(ans) == 7:
        global result
        result.add(ans)
        return

    for k in range(4):
        ni = v[0] + di[k]
        nj = v[1] + dj[k]

        if 0 <= ni < 4 and 0 <= nj < 4:
            find([ni, nj], ans + arr[ni][nj])

for tc in range(1, int(input()) + 1):
    arr = [input().split() for _ in range(4)]
    result = set()
    for i in range(4):
        for j in range(4):
            find([i, j], '')
    print('#{} {}'.format(tc, len(result)))