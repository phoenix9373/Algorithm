N = int(input())

dist = []
for _ in range(6):
    idx, width = map(int, input().split())
    dist.append(width)

areaMax = 0
for i in range(6):
    tmp = dist[i] * dist[(i + 1) % 6]
    if tmp > areaMax:
        areaMax = tmp
        idx = i

areaMin = dist[(idx + 3) % 6] * dist[(idx + 4) % 6]
ans = (areaMax - areaMin) * N
print(ans)