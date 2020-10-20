N = int(input())
arr = [[-1] * 101 for _ in range(101)]
squares = [list(map(int, input().split())) for _ in range(N)]

for idx, loc in enumerate(squares):
    x0, y0, x1, y1 = loc
    for x in range(x0, x0 + x1):
        for y in range(y0, y0 + y1):
            arr[y][x] = idx

for k in range(N):
    cnt = 0
    for i in range(101):
        cnt += arr[i].count(k)
    print(cnt)