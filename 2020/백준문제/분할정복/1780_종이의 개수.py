N = int(input())
maps = [list(map(int, input().split())) for _ in range(N)]
cnt = [0] * 3


def sol(arr):
    global cnt
    check = True
    n = len(arr)
    start = arr[0][0]

    if len(arr) == 1:
        cnt[start + 1] += 1
        return

    for i in range(n):
        for j in range(n):
            if arr[i][j] != start:
                check = False
                break
        if not check:
            break

    if check:
        cnt[start + 1] += 1
    else:
        for i in range(3):
            for j in range(3):
                sol(list(zip(*arr[i*(n//3):(i+1)*(n//3)]))[j*(n//3):(j+1)*(n//3)])


sol(maps)
print(*cnt, sep='\n')