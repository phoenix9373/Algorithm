nums = [list(map(int, input().split())) for _ in range(4)]

X = max(list(zip(*nums))[2])
Y = max(list(zip(*nums))[3])


arr = [[0] * (X + 1) for _ in range(Y + 1)]
for axis in nums:
    x1, y1, x2, y2 = axis
    for x in range(x1, x2):
        for y in range(y1, y2):
            arr[y][x] = 1

print(sum([sum(row) for row in arr]))