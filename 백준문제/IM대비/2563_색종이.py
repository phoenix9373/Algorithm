import sys

N = int(sys.stdin.readline())
axis = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

arr = [[0] * 100 for _ in range(100)] # 빈 리스트

for i, j in axis:
    for x in range(i, i + 10):
        for y in range(j, j + 10):
            arr[y][x] = 1

print(sum([sum(k) for k in arr]))