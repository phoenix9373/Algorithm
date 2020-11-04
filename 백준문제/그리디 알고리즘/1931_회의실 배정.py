N = int(input())
info = sorted([list(map(int, input().split())) for _ in range(N)], key=lambda x: (x[1], x[0]))

cnt = 0
p = 0
for i in range(len(info)):
    tmp = info[i]
    if tmp[0] >= p:
        p = tmp[1]
        cnt += 1
print(cnt)