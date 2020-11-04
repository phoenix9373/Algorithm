N = int(input())

pillar = [0] * 1001
max_H = 0
max_idx = 0
last_idx = 0

for _ in range(N):
    idx, h = map(int, input().split())
    pillar[idx] = h
    if h > max_H:
        max_H = h
        max_idx = idx

curr_H = 0
ans = 0
for i in range(max_idx + 1):
    if pillar[i] > curr_H:
        curr_H = pillar[i]
    ans += curr_H

curr_H = 0
for i in range(1000, max_idx, -1):
    if pillar[i] > curr_H:
        curr_H = pillar[i]
    ans += curr_H
print(ans)